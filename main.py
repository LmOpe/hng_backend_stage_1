import requests

from flask import Flask, request
from flask_cors import CORS

from .utils import (
    is_perfect,
    is_prime,
    sum_digit,
    find_property
)

app = Flask(__name__)
CORS(app)

@app.route("/api/classify-number")
def classify_number():
    number = request.args.get('number')
    base_url = "http://numbersapi.com/"

    if not number:
        return {
            "number": "required",
            "error": True
        }, 400

    try:
        number = int(number)
    except ValueError:
        return {
            "number": "alphabet",
            "error": True
        }, 400

    url = base_url + f"{number}/math"
    fun_fact = requests.get(url)

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": find_property(number),
        "digit_sum": sum_digit(number),
        "fun_fact": fun_fact.text
    }

    return response, 200
