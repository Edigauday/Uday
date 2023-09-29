from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {"id": 52129561, "name": "uday"},
    {"id": 52129559, "name": "asha"}

]


@app.route('/')
def index():
    return " facebook login page"


@app.route("/items", methods=['GET'])
def get():
    return jsonify(dict(items=items))


if __name__ == "__main__":
    app.run(debug=True)
