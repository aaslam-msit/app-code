from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 GitOps Pipeline</h1>
    <p>Status: Running on Kubernetes</p>
    <p>CI/CD with Cloud Build</p>
    <a href='/about'>About</a><br>
    <a href='/status'>Status</a><br>
    <a href='/info'>Pod Info</a>
    """

@app.route("/about")
def about():
    return "This project demonstrates a GitOps CI/CD pipeline using GKE."

@app.route("/status")
def status():
    return "Application is running successfully!"

@app.route("/info")
def info():
    return f"Running on pod: {socket.gethostname()} at {datetime.now()}"

app.run(host="0.0.0.0", port=80)
