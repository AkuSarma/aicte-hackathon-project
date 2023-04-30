from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.get("/questions")
def questions():
    queryList = []
    with open("questions.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            queryList.append(line)

    return render_template("questions.html", queryList = queryList)

if __name__ == "__main__":
    app.run(debug=True)