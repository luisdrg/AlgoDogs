from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    dog_url = None

    if request.method == "POST":
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code == 200:
            dog_url = response.json()["message"]

    return render_template("index.html", dog_url=dog_url)

if __name__ == "__main__":
    app.run(debug=True)
