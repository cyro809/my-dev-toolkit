from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json

    print(payload)

    return {
        "status": "received"
    }

if __name__ == '__main__':
    app.run(port=5000)