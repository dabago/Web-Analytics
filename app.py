# import the Flask class from the flask module
from flask import Flask, render_template, Response, redirect, url_for, request, session, flash, g, jsonify
from functools import wraps
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from flask_cors import CORS
import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import sqlite3

app = Flask(__name__, template_folder="templates")
CORS(app)

# config
# app.secret_key = 'my secret key'


#db connection 
try:
  conn = sqlite3.connect("/Users/dv/Desktop/CloudStation/2018_MCSBT/02_Term/WEB DEVELOPMENT/Individual/individual-assignment-2-dabago/database.db")
  print('Connected to database super well connected')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)


@app.route("/")
def index():
    return render_template('index.html', conn = sqlite3.connect("/Users/dv/Desktop/CloudStation/2018_MCSBT/02_Term/WEB DEVELOPMENT/Individual/individual-assignment-2-dabago/database.db"))

@app.route("/link/<visit>", methods=["POST"])
def register_link2(visit):
    conn = sqlite3.connect("/Users/dv/Desktop/CloudStation/2018_MCSBT/02_Term/WEB DEVELOPMENT/Individual/individual-assignment-2-dabago/database.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS RANKING
   (ID INTEGER PRIMARY KEY AUTOINCREMENT,
   WEBSITE TEXT NOT NULL,
   TIME DATETIME DEFAULT CURRENT_TIMESTAMP);''')
   
    sql = 'INSERT INTO RANKING (WEBSITE) VALUES ("{}")'.format(visit)
    conn.cursor().execute(sql)
    conn.commit()

    return render_template("index.html")


@app.route("/plot.png")
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")

def create_figure():
    conn = sqlite3.connect("/Users/dv/Desktop/CloudStation/2018_MCSBT/02_Term/WEB DEVELOPMENT/Individual/individual-assignment-2-dabago/database.db")
    df = pd.read_sql_query("select * from RANKING;", conn)
    df2 = df[['WEBSITE', 'TIME']].groupby(['WEBSITE']).agg('count').reset_index()

    fig = Figure()

    axis = fig.add_subplot(1, 1, 1)

    xs = df2["WEBSITE"]
    
    ys = df2["TIME"]
    
    axis.set_title("Ranking Link Visits")

    axis.plot(xs, ys)
    
    return fig





if __name__ == '__main__':
    app.run(debug=True)