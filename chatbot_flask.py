# chatbot_flask.py
from flask import Flask, render_template, request
from healthcare_data import DISEASE_DB, KEYWORD_INDEX
import re, difflib

app = Flask(__name__)

def tokenize(text):
    return re.findall(r'\b[a-z0-9]+\b', text.lower())

def find_disease_by_name_or_alias(query):
    q = query.lower()
    for disease, info in DISEASE_DB.items():
        names = [disease] + info.get("aliases", [])
        for n in names:
            if n in q:
                return disease, 1.0
    diseases = list(DISEASE_DB.keys())
    matches = difflib.get_close_matches(q, diseases, n=1, cutoff=0.8)
    if matches:
        return matches[0], 0.8
    return None, 0.0

def find_disease_by_symptoms(query_tokens):
    scores = []
    for disease, tokens in KEYWORD_INDEX.items():
        overlap = len(set(query_tokens) & set(tokens))
        if overlap > 0:
            scores.append((disease, overlap))
    scores.sort(key=lambda x: x[1], reverse=True)
    if not scores:
        return None, 0
    return scores[0]

def format_response_html(disease, info, score=None):
    html = f"<h3>Information: {disease.capitalize()}</h3>"
    html += f"<p><b>Symptoms:</b> {info['symptoms']}</p>"
    html += f"<p><b>Medicines / Treatment (informational):</b> {info['medicines']}</p>"
    html += f"<p><b>Precautions:</b> {info.get('precautions','Follow doctor guidance.')}</p>"
    if info.get("serious"):
        html += f"<p style='color:darkred'><b>⚠️ This condition can be serious. Please consult a {info.get('specialist','specialist')}.</b></p>"
    if score:
        html += f"<p><i>Match confidence: {score}</i></p>"
    return html

@app.route('/', methods=['GET','POST'])
def home():
    response_html = ""
    query = ""
    if request.method == 'POST':
        query = request.form.get('query','').strip()
        if query:
            q_tokens = tokenize(query)
            # try disease name
            disease, conf = find_disease_by_name_or_alias(query)
            if disease:
                response_html = format_response_html(disease, DISEASE_DB[disease], score=conf)
            else:
                # symptom match
                top = find_disease_by_symptoms(q_tokens)
                if top and top[1] >= 1:
                    response_html = ("<p>Based on symptoms you described, a possible match is:</p>"
                                     + format_response_html(top[0], DISEASE_DB[top[0]], score=top[1]))
                else:
                    # optional web fallback (Wikipedia) -- only if package installed & internet
                    try:
                        import wikipedia
                        titles = wikipedia.search(query, results=1)
                        if titles:
                            summary = wikipedia.summary(titles[0], sentences=2)
                            response_html = ("<p>I couldn't find a close match in my local database. "
                                             "Here is a short web summary (educational):</p>"
                                             f"<p>{summary}</p>"
                                             "<p><i>Note: this is a web summary — consult a doctor for personalized advice.</i></p>")
                        else:
                            response_html = "<p>Sorry — I don't have information for that query. Please rephrase or consult a healthcare professional.</p>"
                    except Exception:
                        response_html = "<p>Sorry — I don't have information for that query in the local database. Web lookup is unavailable.</p>"

    return render_template('index.html', response_html=response_html, query=query)

if __name__ == "__main__":
    app.run(debug=True)
