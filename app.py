# app.py
from flask import Flask, render_template, request, session
from healthcare_data import DISEASE_DB, KEYWORD_INDEX
import wikipedia
import difflib
import re
import logging

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Logging
logging.basicConfig(filename="chatbot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# -----------------------------
# Utility functions
# -----------------------------
def tokenize(text):
    return re.findall(r'\b[a-z0-9]+\b', text.lower())

def find_disease_by_name_or_alias(query):
    q = query.lower()
    for disease, info in DISEASE_DB.items():
        names = [disease] + info.get("aliases", [])
        for n in names:
            if n in q:
                return disease, 1.0
    matches = difflib.get_close_matches(q, list(DISEASE_DB.keys()), n=1, cutoff=0.8)
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
    return scores[0] if scores else (None, 0)

def format_response(disease, info, score=None, html=True):
    if html:
        s = f"<h3>Information: {disease.capitalize()}</h3>"
        s += f"<p><b>Symptoms:</b> {info['symptoms']}</p>"
        s += f"<p><b>Medicines / Treatment:</b> {info['medicines']}</p>"
        s += f"<p><b>Precautions:</b> {info.get('precautions','Follow doctor guidance.')}</p>"
        if info.get("serious"):
            s += f"<p style='color:darkred'><b>⚠️ Serious: Consult {info.get('specialist','specialist')}.</b></p>"
        if score:
            s += f"<p><i>Match confidence: {score}</i></p>"
    else:
        s = f"--- Information: {disease.capitalize()} ---\n"
        s += f"Symptoms: {info['symptoms']}\n"
        s += f"Medicines / Treatment: {info['medicines']}\n"
        s += f"Precautions: {info.get('precautions','Follow doctor guidance.')}\n"
        if info.get("serious"):
            s += f"⚠️ Serious: Consult {info.get('specialist','specialist')}.\n"
        if score:
            s += f"(Match confidence: {score})\n"
    return s

def fetch_wikipedia_summary(query, html=True):
    try:
        title = wikipedia.search(query, results=1)
        if title:
            summary = wikipedia.summary(title[0], sentences=2)
            if html:
                return f"<p><b>Info from Wikipedia:</b> {summary}</p>"
            return f"Info from Wikipedia:\n{summary}"
    except Exception:
        return None
    return None

def handle_query(query, html=True):
    query_tokens = tokenize(query)
    disease, conf = find_disease_by_name_or_alias(query)
    if disease:
        return format_response(disease, DISEASE_DB[disease], score=conf, html=html)
    top_disease, score = find_disease_by_symptoms(query_tokens)
    if top_disease and score >= 1:
        response = ("<p>Based on symptoms you described, possible match:</p>" if html
                    else "Based on symptoms you described, possible match:\n")
        response += format_response(top_disease, DISEASE_DB[top_disease], score=score, html=html)
        return response
    wiki_summary = fetch_wikipedia_summary(query, html=html)
    if wiki_summary:
        return wiki_summary
    return ("<p>Sorry, I couldn't find information for your query. Please rephrase or consult a healthcare professional.</p>"
            if html else "Sorry, I couldn't find information for your query. Please rephrase or consult a healthcare professional.")

# -----------------------------
# Flask routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    if "chat_history" not in session:
        session["chat_history"] = []

    response_html = ""
    query = ""
    if request.method == "POST":
        query = request.form.get("query", "").strip()
        if query:
            response_html = handle_query(query, html=True)
            
            # Save to session
            session["chat_history"].append(("user", query))
            session["chat_history"].append(("bot", response_html))
            session.modified = True

            # Log to file
            logging.info(f"Query: {query} | Response: {response_html[:100]}")

            # Print live in console
            print(f"\nUser: {query}")
            print(f"Bot: {re.sub('<[^<]+?>', '', response_html)}\n")  # strip HTML for console

    return render_template("index.html",
                           chat_history=session.get("chat_history", []),
                           query=query,
                           response_html=response_html)

if __name__ == "__main__":
    # Print the access URL in the terminal
    print("\n🚀 Healthcare Chatbot is running!")
    print("Open this link in your browser to start chatting:")
    print("http://127.0.0.1:5000\n")

    # Start Flask server
    app.run(debug=True)