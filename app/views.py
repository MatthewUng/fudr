from app import app
from flask import render_template, request, redirect, url_for
import hashlib


temp = {"hello": 0,
        "world": 1}

@app.route('/', methods=['GET'])
def index():
    print("in index")
    print(request.method)
    error = request.args.get('error')
    if error:
        return render_template('index.html', error=error)
    else:
        return render_template('nidex.html')

@app.route("/create/", methods=['GET', 'POST'])
def vote_create():
    print("in vote_create")
    print(request.method)
    return render_template('vote_create.html')

@app.route("/join/<int:value>", methods=['GET', 'POST'])
def join_vote(value):
    print("join_vote")
    print(request.method)
    return render_template('join_vote.html', group_num=value)

@app.route("/redirect/", methods=['POST'])
def join_redirect():
    print('in redirect')
    print(request.method)
    if request.form['group name']:
        key = request.form['group name']
        num = temp[key]
        return redirect(url_for('join_vote',value=num))
    else:
        return redirect(url_for('index', error="No input was detected!"))
    return "help"
