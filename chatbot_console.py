# chatbot_console.py
import re
import difflib
from healthcare_data import DISEASE_DB, KEYWORD_INDEX

def tokenize(text):
    return re.findall(r'\b[a-z0-9]+\b', text.lower())

def find_disease_by_name_or_alias(query):
    # direct substring match (preferred)
    q = query.lower()
    for disease, info in DISEASE_DB.items():
        # check name and aliases
        names = [disease] + info.get("aliases", [])
        for n in names:
            if n in q:
                return disease, 1.0
    # fuzzy match on disease names
    diseases = list(DISEASE_DB.keys())
    matches = difflib.get_close_matches(q, diseases, n=1, cutoff=0.8)
    if matches:
        return matches[0], 0.8
    return None, 0.0

def find_disease_by_symptoms(query_tokens):
    # Score diseases by token overlap with symptom keywords
    scores = []
    for disease, tokens in KEYWORD_INDEX.items():
        overlap = len(set(query_tokens) & set(tokens))
        if overlap > 0:
            scores.append((disease, overlap))
    scores.sort(key=lambda x: x[1], reverse=True)
    if not scores:
        return None, 0
    # return top candidate and its overlap score
    top, score = scores[0]
    return top, score

def format_response(disease, info, score=None):
    s = []
    s.append(f"--- Information: {disease.capitalize()} ---")
    s.append(f"Symptoms: {info['symptoms']}")
    s.append(f"Suggested (informational) medicines/treatment: {info['medicines']}")
    s.append(f"Precautions: {info.get('precautions','Follow doctor guidance.')}")
    if info.get("serious"):
        s.append(f"⚠️ This condition can be serious. Please consult a {info.get('specialist','specialist')}.")
    if score:
        s.append(f"(Match confidence: {score})")
    return "\n".join(s)

def web_fallback_summary(query):
    # optional: tries to fetch a short summary from wikipedia (if the package is installed)
    try:
        import wikipedia
        wikipedia.set_lang("en")
        title = wikipedia.search(query, results=1)
        if title:
            summary = wikipedia.summary(title[0], sentences=2)
            return summary
    except Exception:
        return None
    return None

def handle_query(query):
    q = query.lower()
    q_tokens = tokenize(q)

    # 1) try direct disease name / alias match
    disease, conf = find_disease_by_name_or_alias(q)
    if disease:
        return format_response(disease, DISEASE_DB[disease], score=conf)

    # 2) if user asked "what are the symptoms" or similar, try symptom matching
    symptom_keywords = {"symptom", "symptoms", "signs", "feel", "having", "i have", "i'm having"}
    if any(k in q for k in symptom_keywords) or len(q_tokens) <= 6:
        top, score = find_disease_by_symptoms(q_tokens)
        if top and score >= 1:
            # If low token overlap but better than nothing, show probable match
            return ("Based on your described symptoms, you may have: \n"
                    + format_response(top, DISEASE_DB[top], score=score))
    # 3) if user asked about medicine/treatment
    if "medicine" in q or "treatment" in q or "drug" in q:
        # attempt symptom-based match again
        top, score = find_disease_by_symptoms(q_tokens)
        if top:
            return format_response(top, DISEASE_DB[top], score=score)

    # 4) fallback: try to guess from keywords (looser)
    top, score = find_disease_by_symptoms(q_tokens)
    if top and score >= 1:
        return format_response(top, DISEASE_DB[top], score=score)

    # 5) optional web fallback (Wikipedia) — will succeed only if 'wikipedia' is installed & internet active
    web_summary = web_fallback_summary(query)
    if web_summary:
        return ("I couldn't find a close match in my local database. Here's a short web summary (educational):\n\n"
                + web_summary + "\n\nNote: this is a web summary — consult a doctor for personalized advice.")

    return ("Sorry — I don't have information for that query. "
            "Please rephrase (e.g., 'What are symptoms of diabetes?' or 'I have fever and rash') "
            "or consult a healthcare provider.")

def run_console():
    print("🩺 Healthcare Chatbot (console). Type 'exit' to quit.")
    while True:
        query = input("You: ").strip()
        if not query:
            continue
        if query.lower() in ("exit", "quit"):
            print("Bot: Take care! This chatbot is for informational use only. Consult a doctor for medical advice.")
            break
        response = handle_query(query)
        print("\nBot:", response, "\n")

if __name__ == "__main__":
    run_console()
