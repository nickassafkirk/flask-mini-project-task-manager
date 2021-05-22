import os
from flask import Flask
if os.path.exists("env.py"):
    import env
    # when we deploy project to flask it will throw error
    # if it can't find env.py file. this is why we need if
    # statement.


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)  # change debug to false before deploying

