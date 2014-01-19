from flask import Blueprint, render_template, redirect, request, current_app, session, flash, url_for
from app import app, db
from flask_oauthlib.client import OAuth
from app.user.models import User

oauth = OAuth(app)
facebook = oauth.remote_app(
    'facebook',
    consumer_key=app.config['FACEBOOK_APP_ID'],
    consumer_secret=app.config['FACEBOOK_APP_SECRET'],
    request_token_params=app.config['FACEBOOK_APP_PARAMS'],
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth'
)

mod = Blueprint('userModule', __name__)

@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or redirect('/'),
        _external=True))


@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    session['logged_in'] = True
    me = facebook.get('/me')
    user = User.query.filter_by(email=me.data['email']).first()
    if user is None:
        user = User(me.data['email'],'facebook',me.data['id'],resp['access_token'],me.data['name'],me.data['link'])
        db.session.add(user)
        db.session.commit()
        session['id'] = user.id
    else :
        user.access_token = resp['access_token']
        db.session.add(user)
        db.session.commit()

    session['id'] = user.id
    session['name'] = user.name

    """return 'Logged in as id=%s name=%s email=%s redirect=%s' % \
        (me.data['id'], me.data['name'], me.data['email'], request.args.get('next'))"""
    return redirect('/')

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('oauth_token', None)
    session.pop('id', None)
    session.pop('name', None)

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect('/')