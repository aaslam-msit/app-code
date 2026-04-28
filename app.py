from flask import Flask, request, redirect
import socket
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        msg = request.form.get("msg")
        if msg:
            messages.append(msg)
        return redirect("/")

    msg_list = "".join([f"<li>{m}</li>" for m in messages])

    return f"""
    <html>
    <head>
        <title>GitOps App</title>
        <style>
            body {{
                font-family: Arial;
                background: #f4f6f9;
                text-align: center;
                padding: 40px;
