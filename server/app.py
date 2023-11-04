from flask import Flask, render_template, request, redirect, flash, jsonify

app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def hello():
    """Hello world."""
    return "<h1>hello guys this is awesome</h1>"


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
