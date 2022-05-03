from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = "s3secret"

def connectSQL():
    conn = sql.connect(r"/Users/suhninlwin/Visual Studio Code/MyFirstDemo/firstdemo.db")
    conn.row_factory = sql.Row
    return conn


@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True, port=5551)
