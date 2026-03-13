from flask import Flask

app = Flask(__name__)

def hello():
    return "CI/CD Pipeline Triggered"

@app.route("/")
def home():
    return hello()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
