# chatbotflask.py
# A simpler Flask web app, reusing console logic
from flask import Flask, render_template, request, session
from chatbotconsole import handle_query  # reuse the console logic
import logging

app = Flask(__name__)
app.secret_key = "your_secret_key"

logging.basicConfig(filename="chatbot.log", level=logging.INFO)

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat_history" not in session:
        session["chat_history"] = []

    response_html = ""
    query = ""
    if request.method == "POST":
        query = request.form.get("query", "").strip()
        if query:
            response_html = handle_query(query)
            session["chat_history"].append(("user", query))
            session["chat_history"].append(("bot", response_html))
            session.modified = True
            logging.info(f"Query: {query} | Response: {response_html[:100]}")

    # Complete the render_template call
    return render_template("index.html",
                           chat_history=session.get("chat_history", []),
                           query=query,
                           response_html=response_html)

if __name__ == "__main__":
    app.run(debug=True)
