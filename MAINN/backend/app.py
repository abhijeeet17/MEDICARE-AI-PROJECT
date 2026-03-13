from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Medicare AI Running"

if __name__ == "__main__":
    app.run()