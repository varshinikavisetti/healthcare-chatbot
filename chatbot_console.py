# chatbotconsole.py
from healthcare_data import DISEASE_DB, KEYWORD_INDEX
import wikipedia
import difflib
import re

# -----------------------------
# Same utility functions as in app.py
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

def format_response(disease, info, score=None, html=False):
    if html:
        return f"<h3>Information: {disease}</h3>"
    s = f"--- Information: {disease.capitalize()} ---\n"
    s += f"Symptoms: {info['symptoms']}\n"
    s += f"Medicines / Treatment: {info['medicines']}\n"
    s += f"Precautions: {info.get('precautions','Follow doctor guidance.')}\n"
    if info.get("serious"):
        s += f"⚠️ Serious: Consult {info.get('specialist','specialist')}.\n"
    if score:
        s += f"(Match confidence: {score})\n"
    return s

def fetch_wikipedia_summary(query):
    try:
        title = wikipedia.search(query, results=1)
        if title:
            summary = wikipedia.summary(title[0], sentences=2)
            return f"Info from Wikipedia:\n{summary}"
    except Exception:
        return None
    return None

def handle_query(query):
    query_tokens = tokenize(query)
    disease, conf = find_disease_by_name_or_alias(query)
    if disease:
        return format_response(disease, DISEASE_DB[disease], score=conf)
    top_disease, score = find_disease_by_symptoms(query_tokens)
    if top_disease and score >= 1:
        return "Based on symptoms you described, possible match:\n" + \
               format_response(top_disease, DISEASE_DB[top_disease], score=score)
    wiki_summary = fetch_wikipedia_summary(query)
    if wiki_summary:
        return wiki_summary
    return "Sorry, I couldn't find information for your query. Please rephrase or consult a healthcare professional."

# -----------------------------
# Console chatbot
# -----------------------------
def run_console():
    print("🩺 Healthcare Chatbot (console). Type 'exit' to quit.")
    while True:
        query = input("You: ").strip()
        if not query:
            continue
        if query.lower() in ("exit", "quit"):
            print("Bot: Take care! Consult a doctor for medical advice.")
            break
        response = handle_query(query)
        print("\nBot:", response, "\n")

if __name__ == "__main__":
    run_console()
