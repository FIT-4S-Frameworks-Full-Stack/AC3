from flask import Flask, render_template, request


# APLICAÇÃO FLASK
app = Flask(__name__)





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='localhost', port=port, debug=True)
