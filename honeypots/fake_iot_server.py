from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"device": "IoT Camera", "status": "active"})

@app.route('/data')
def data():
    return jsonify({
        "temperature": random.randint(20,40),
        "humidity": random.randint(40,80)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)