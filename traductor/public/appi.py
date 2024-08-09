from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable global para almacenar el último mensaje recibido
last_message = None

@app.route('/receive', methods=['POST'])
def receive_message():
    global last_message
    data = request.json
    message = data.get('message')

    if not message:
        return jsonify({"error": "Missing 'message' in request"}), 400

    last_message = message
    return jsonify({"status": "Message received", "message": last_message})

@app.route('/consume', methods=['GET'])
def consume_message():
    global last_message

    if last_message is None:
        return jsonify({"error": "No message available"}), 404

    # Return the last message received
    return jsonify({"message": last_message})

if __name__ == '__main__':
    app.run(debug=True)
