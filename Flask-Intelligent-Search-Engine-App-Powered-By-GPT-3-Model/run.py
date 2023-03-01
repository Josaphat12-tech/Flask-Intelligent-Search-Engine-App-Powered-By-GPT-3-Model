from flask import Flask, request, render_template
import openai

#Author : Bitingo Josaphat JB
#github : https://www.github.com/Josaphat12-tech

API_KEY = "Go Pick your Api Key"
app = Flask(__name__)
openai.api_key = API_KEY

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question")
        answer = chat_bot(question)
        chat_history.append((question, answer))
    return render_template("index.html", chat_history=chat_history)

def chat_bot(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=2048,
        n=1,
    )
    message = response.choices[0].text
    return message.strip()

if __name__ == "__main__":
    app.run(debug=True)
