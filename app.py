from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""

    if request.method == "POST":
        user_query = request.form["query"]

        prompt = f"""
        You are an AI Airport Passenger Assistant.

        Answer the passenger query professionally.

        Query:
        {user_query}
        """

        response = model.generate_content(prompt)
        response_text = response.text

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)