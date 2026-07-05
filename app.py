from flask import Flask, redirect, render_template, request, session, url_for, make_response, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'vovavovavova'



@app.route("/")
def index():
    if 'clicks' not in session:
        session['clicks'] = 0
    

    return render_template(
        "index.html",
        cnt = session['clicks']
    )

@app.route("/click", methods=['POST'])
def click():
    session['clicks'] += 1
    return jsonify({'clicks': session['clicks']})

@app.route("/reset", methods=['POST'])
def reset():
    session['clicks'] = 0
    return jsonify({'clicks': 0})



if __name__ == "__main__":
    app.run(debug=True)