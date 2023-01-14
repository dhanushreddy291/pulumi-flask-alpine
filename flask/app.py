from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "A Flask App made using Docker and Pulumi"