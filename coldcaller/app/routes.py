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

    with open('sample.txt') as f:
        names = [name.strip() for name in f.readlines()]
    cc = ColdCaller(names)
    

    fig, ax = plt.subplots()
    ax.barh(list(cc.students.keys()), cc.students.values())

    
    plt.savefig("templates/foo.html", format='svg')
    return render_template('foo.html')
