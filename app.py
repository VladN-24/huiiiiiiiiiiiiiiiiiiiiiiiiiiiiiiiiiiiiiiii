from flask import Flask, redirect, render_template, request, session, url_for, make_response, jsonify


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
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)