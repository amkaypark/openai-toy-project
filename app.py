import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        response = openai.Completion.create(
            model="text-ada-001",
            prompt=generate_prompt(ingredients),
            temperature=0.6,
            max_tokens=100
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(ingredients):
    return """Suggest a dish and recipe for it using {}. Put the dish name first and give steps to make the recipe in a list format.
Recipe:""".format(
        ingredients.capitalize()
    )
