import sentry_sdk
from flask import Flask, render_template

sentry_sdk.init(
    dsn="https://2202721634f7017e585a58b72c56f7c7@o4509990068027392.ingest.us.sentry.io/4510002564825088",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/tela_cadastro")
def tela_cadastro():
    return render_template("tela_cadastro.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)