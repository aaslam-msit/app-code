from flask import Flask, request, redirect
import socket
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect("/")

    task_list = "".join([
        f"<li>{t} <a href='/delete/{i}'>❌</a></li>"
        for i, t in enumerate(tasks)
    ])

    return f"""
<html>
<head>
<title>TODO App</title>
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
    width: 400px;
    margin: auto;
}}
input {{
    padding: 10px;
    width: 70%;
}}
button {{
    padding: 10px;
    background: green;
    color: white;
    border: none;
}}
li {{
    list-style: none;
    margin: 5px;
}}
</style>
</head>
<body>

<div class="container">
    <h1>📝 TODO App - Demo</h1>

    <form method="POST">
        <input name="task" placeholder="Enter task..." />
        <button>Add</button>
    </form>

    <ul>{task_list}</ul>

    <p>Pod: {socket.gethostname()}</p>
    <p>Time: {datetime.now()}</p>
</div>

</body>
</html>
"""

@app.route("/delete/<int:index>")
def delete(index):
    if index < len(tasks):
        tasks.pop(index)
    return redirect("/")

app.run(host="0.0.0.0", port=8080)
