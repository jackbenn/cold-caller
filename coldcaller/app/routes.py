import os
from flask import render_template
from flask import Flask
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from src.coldcaller import ColdCaller
matplotlib.use('Agg')

app = Flask(__name__)


@app.route('/coldcaller/')
def index():
    cc = ColdCaller()
    if os.path.isfile('state.txt'):
        cc.read_state('state.txt')
    else:
        cc.read_names('sample.txt')

    winner = cc.choose()
    cc.write_state('state.txt')

    fig, ax = plt.subplots()
    ax.barh(list(cc.students.keys()), cc.students.values())
    ax.set_xlabel('probability of being called on next')
    ax.set_ylabel('name')

    
    plt.savefig("chart.svg", format='svg')
    with open('chart.svg') as f:
        svg = f.read()
    return render_template('index.html', svg=svg, winner=winner)
