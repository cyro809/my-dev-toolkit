from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ])

if __name__ == "__main__":
    app.run(debug=True)