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
            }}
            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                width: 400px;
                margin: auto;
            }}
            h1 {{
                color: #333;
            }}
            input {{
                padding: 10px;
                width: 70%;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            button {{
                padding: 10px 15px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{
                background: #0056b3;
            }}
            ul {{
                list-style: none;
                padding: 0;
            }}
            li {{
                background: #e9ecef;
                margin: 5px;
                padding: 10px;
                border-radius: 5px;
            }}
            .info {{
                margin-top: 15px;
                font-size: 14px;
                color: #666;
            }}
        </style>
    </head>
    <body>

        <div class="container">
            <h1>🚀 GitOps Dynamic App</h1>

            <form method="POST">
                <input name="msg" placeholder="Enter message"/>
                <button type="submit">Add</button>
            </form>

            <h3>Messages</h3>
            <ul>{msg_list}</ul>

            <div class="info">
                Running on pod: {socket.gethostname()} <br>
                Time: {datetime.now()}
            </div>
        </div>

    </body>
    </html>
    """

app.run(host="0.0.0.0", port=80)
