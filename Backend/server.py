from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    #get and send json
    return "Test Route"

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
