from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello everyone  from Jenkins + Docker + GitHub is sucessfully 🐼fdgfdg!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
               