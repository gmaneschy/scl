import sentry_sdk
from flask import Flask, render_template
from flask_wtf import CSRFProtect

import forms

sentry_sdk.init(
    dsn="https://2202721634f7017e585a58b72c56f7c7@o4509990068027392.ingest.us.sentry.io/4510002564825088",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

import os
app = Flask(__name__)
app.config['SECRET_KEY'] = '6029H039HVF093V5B6091HUVHSDPO89YP8Y2PUIHBSUFGHVB02BVHUS'
csrf = CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
def tel_cadastro():
    form_cadprof = forms.CadProf()
    return render_template("tela_cadastro.html", form_cadprof = form_cadprof)

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
