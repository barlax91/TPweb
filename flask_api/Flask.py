import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from flask import Flask, app, url_for
from werkzeug.utils import redirect

app = Flask('__name__')

df = pd.read_csv('vgsales.csv')


@app.route("/")
def index():
    return "<h1>Crash course Flask<"


@app.route('/hello')
def hello():
    return 'Hello, World '


@app.route('/user')
def user():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
