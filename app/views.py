from app import app, db
from app.models import Group, Restaurant
from flask import render_template, request, redirect, url_for
from sqlalchemy.sql.expression import func, select
from .YelpAPI import getRestaurants
from urllib.parse import quote_plus
from .charts import create_chart

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

@app.route("/<group_url>", methods=['GET'])
def view_group(group_url):
    print("in view_group")
    print(request.method)

    db_group = db.session.query(Group).filter_by(url=group_url).first()
    plot_script, plot_div = create_chart(db_group)
    print("found: {}".format(db_group.name))

    return render_template('group_view.html',
                           group=db_group,
                           plot_div=plot_div,
                           plot_script=plot_script)

@app.route("/create_redirect/", methods=['POST'])
def create_redirect():
    print("in create_redirect")
    print(request.method)
    name = request.form['group name']
    result = db.session.query(Group).filter_by(name=name).first()
    if result:
        #group already exists
        print("already exists!")
        print(result)
        return redirect(url_for('index', error="group already exists!"))
    else:
        url_friendly = quote_plus(name.strip())
        g = Group(name, url_friendly)
        restaurants = getRestaurants(app.config['BEARER_TOKEN'])
        for r in restaurants:
            new = Restaurant(r['name'], r['url'], r['image_url'])
            db.session.add(new)
            g.restaurants.append(new)
        db.session.add(g)
        db.session.commit()
        db.session.close()
        return redirect(url_for('view_group', group_url=url_friendly))

@app.route("/join_redirect/", methods=['POST'])
def join_redirect():
    print('in join_redirect')
    print(request.method)
    if 'group name' in request.form:
        key = request.form['group name']
        r = db.session.query(Group).filter_by(name=key).first()
        if not r:
            return redirect(url_for('index', error="Group not found!"))
        print(r.url)
        return redirect('/'+r.url)
    else:
        return redirect(url_for('index', error="No input was detected!"))

@app.route("/vote_redirect/", methods=['POST'])
def vote_redirect():
    print("in vote_redirect")
    print(request.method)
    if 'vote' in request.form:
        r_name = request.form['vote']
        g_name = request.form['group']
        g = db.session.query(Group).filter_by(name=g_name).first()
        r = db.session.query(Restaurant).filter_by(owner_group=g, name=r_name).first()
        r.count += 1
        db.session.commit()
        return redirect(url_for('view_group', group_url=g.url))
    else:
        return redirect(url_for('index', error="no vote was detected"))

