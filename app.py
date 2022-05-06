import os
from flask import Flask, render_template, request


# APLICAÇÃO FLASK
app = Flask(__name__)


# CONTROLLERS
@app.route('/')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='localhost', port=port, debug=True)
