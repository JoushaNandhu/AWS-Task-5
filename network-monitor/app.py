from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

@app.route('/')
def home():
    with open('devices.json', 'r') as file:
        devices = json.load(file)
    # Randomly change some statuses to simulate live updates
    for d in devices:
        d['status'] = random.choice(['Online', 'Offline', 'Active', 'Idle'])
    return render_template('index.html', devices=devices)

@app.route('/api/devices')
def get_devices():
    with open('devices.json', 'r') as file:
        devices = json.load(file)
    return jsonify(devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
