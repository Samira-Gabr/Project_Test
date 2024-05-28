#Create a simple web interface using Flask.
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('alerts.json', 'r') as f:
        alerts = json.load(f)
    return render_template('index.html', alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)
