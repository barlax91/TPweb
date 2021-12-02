import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from flask import Flask, app

app = Flask('__name__')

df = pd.read_csv('vgsales.csv')


@app.route("/")
def index():

    return "Crash course Flask"


@app.route('/hello')
def hello():
    return 'Hello, World '


if __name__ == '__main__':
    app.run(debug=True)
