from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated in-memory user store and balance
users = []
balance = 1000

# 1️⃣ Service status endpoint
@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "service": "Telecom Messaging API",
        "status": "running"
    })

# 2️⃣ Health check endpoint for Kubernetes
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "service": "Telecom Messaging API",
        "health": "healthy"
    })

# 3️⃣ Send message
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

# 4️⃣ Check SMS balance
@app.route('/check-balance', methods=['GET'])
def check_balance():
    return jsonify({
        "sms_balance": balance
    })

# 5️⃣ Create a new user
@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.json
    user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "number": data.get("number")
    }
    users.append(user)

    return jsonify({
        "message": "User created",
        "user": user
    })

# 6️⃣ List all users
@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(users)

# 7️⃣ Delete a user by ID
@app.route('/delete-user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]

    return jsonify({
        "message": "User deleted"
    })

# 8️⃣ Recharge SMS balance
@app.route('/recharge', methods=['POST'])
def recharge():
    global balance
    data = request.json
    amount = data.get("amount", 0)
    balance += amount

    return jsonify({
        "message": "Balance updated",
        "new_balance": balance
    })

# 9️⃣ Check message delivery status
@app.route('/message-status/<msg_id>', methods=['GET'])
def message_status(msg_id):
    return jsonify({
        "message_id": msg_id,
        "status": "Delivered"
    })

# 🔟 Delivery report
@app.route('/delivery-report', methods=['GET'])
def delivery_report():
    return jsonify({
        "total_messages": 120,
        "delivered": 118,
        "failed": 2
    })

# 1️⃣1️⃣ Service information
@app.route('/service-info', methods=['GET'])
def service_info():
    return jsonify({
        "service": "Telecom Messaging API",
        "version": "1.0",
        "provider": "Telecom DevOps Platform"
    })

# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)