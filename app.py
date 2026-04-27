from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "GitOps Pipeline WORKING AUTO!"

app.run(host="0.0.0.0", port=80)
