from flask import Flask

app = Flask(__name__)

def hello():
    return "Hello from CI/CD Pipeline with Jenkins + SonarQube + Docker!"

@app.route("/")
def home():
    return hello()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
