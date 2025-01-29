from flask import Flask, request
from sieve import Sieve


# Load our prime numbers at runtime
sieve = Sieve()

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def result():
    if request.method == "GET":
        return 'Please send a post request with json like \'{\"number\": 19}\'', 200
    if request.method == "POST":
        res = request.get_json(force=True)
        n = res["number"]
        prime_num = sieve.nth_prime(n)
        return f"{prime_num}", 200
