from flask import Flask
from prometheus_client import Counter, generate_latest
import random
import uuid

app = Flask(__name__)


checkout = Counter(
    "checkout_total",
    "checkout transactions",
    [
        "user_id",
        "session_id",
        "payment",
        "country"
    ]
)


@app.route("/")
def home():
    return "Mimir High Cardinality Demo"


@app.route("/buy")
def buy():

    checkout.labels(
        user_id=str(uuid.uuid4()),
        session_id=str(random.randint(1,1000000)),
        payment=random.choice(["visa","upi"]),
        country="india"
    ).inc()

    return "checkout done"


@app.route("/metrics")
def metrics():
    return generate_latest()


app.run(
    host="0.0.0.0",
    port=5000
)
