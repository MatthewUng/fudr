from app import app, db
from app.models import Group, Restaurant
from flask import render_template, request, redirect, url_for
from sqlalchemy.sql.expression import func, select
from .YelpAPI import getRestaurants


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
        return render_template('index.html')

@app.route("/create/", methods=['GET', 'POST'])
def create_vote():
    print("in create_vote")
    print(request.method)
    return render_template('create_vote.html')

@app.route("/<group>", methods=['GET'])
def view_group(group):
    print("in view_group")
    print(request.method)

    db_group = db.session.query(Group).filter_by(name=group).first()

    print("found: {}".format(db_group.name))

    return render_template('group_view.html', group=db_group)

@app.route("/redirect/", methods=['POST'])
def create_redirect():
    print("in create_redirect")
    print(request.method)
    name = request.form['group name']
    result = db.session.query(Group).filter_by(name=name).first()
    # db.session.close()
    if result:
        #group already exists
        print("already exists!")
        print(result)
        return redirect(url_for('index'))
    else:
        g = Group(name)
        restaurants = getRestaurants(app.config['bearer_token'])
        for r in restaurants:
            new = Restaurant(r['name'], r['url'])
            db.session.add(new)
            g.restaurants.append(new)
        db.session.add(g)
        db.session.commit()
        db.session.close()
        return redirect(url_for('view_group', group=name))

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

@app.route("/groupview", methods=['GET'])
def group_view():
    return render_template('group_view.html')
