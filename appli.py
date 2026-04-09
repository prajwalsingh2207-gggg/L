from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Phase 1: ho ho ho ho oh oh oh oh "

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
