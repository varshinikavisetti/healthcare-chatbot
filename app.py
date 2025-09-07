from flask import Flask, render_template, request, session
from healthcare_data import DISEASE_DB
import wikipedia

app = Flask(__name__)
app.secret_key = "your_secret_key"

def find_disease(query: str):
    query = query.lower()
    for disease, info in DISEASE_DB.items():
        # check aliases
        if any(alias in query for alias in info.get("aliases", [])):
            return disease, info
        # check symptom keywords
        if any(symptom.strip() in query for symptom in info.get("symptoms", "").split(",")):
            return disease, info
    return None, None

def fetch_from_wikipedia(query: str):
    try:
        summary = wikipedia.summary(query, sentences=2, auto_suggest=True, redirect=True)
        return f"🌐 <b>Info from Wikipedia:</b><br>{summary}"
    except Exception:
        return "❌ I couldn’t find reliable information online either. Please consult a doctor."

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        query = request.form["query"]
        session["chat_history"].append(("user", query))

        disease, info = find_disease(query)
        if disease:
            response = (
                f"<b>Disease:</b> {disease.capitalize()}<br>"
                f"<b>Symptoms:</b> {info['symptoms']}<br>"
                f"<b>Medicines:</b> {info['medicines']}<br>"
                f"<b>Precautions:</b> {info['precautions']}<br>"
            )
            if info["serious"]:
                response += f"<b>⚠️ Please consult a {info['specialist']}.</b>"
        else:
            # fallback to Wikipedia search
            response = fetch_from_wikipedia(query)

        session["chat_history"].append(("bot", response))
        session.modified = True

    return render_template("index.html", chat_history=session["chat_history"])

if __name__ == "__main__":
    app.run(debug=True)
