from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "service": "Telecom Messaging API",
        "status": "running"
    })

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.json

    number = data.get("number")
    message = data.get("message")

    return jsonify({
        "number": number,
        "message": message,
        "status": "Message sent successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)