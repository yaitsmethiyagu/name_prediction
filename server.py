from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html" , name = "Thiyagu")


@app.route("/<name>")
def guess(name):
    name_prediction = requests.get(f"https://api.agify.io/?name={name}&country_id=IN")
    sex_prediction = requests.get(f"https://api.genderize.io/?name={name}&country_id=IN")

    name_prediction = name_prediction.json()
    sex_prediction = sex_prediction.json()

    age = name_prediction["age"]
    count = name_prediction["count"]
    name = name.capitalize()
    sex = sex_prediction["gender"]
    print(name_prediction)
    return render_template("result.html", age= age , count= count, name= name, sex= sex)

if __name__ == "__main__":
    app.run(debug=True)


