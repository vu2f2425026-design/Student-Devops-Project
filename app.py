from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h2>Student Information System</h2><h3>DevOps Pipeline Successfully Executed</h3>"


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
