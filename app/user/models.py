from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))

    def __init__(self, email, provider_id, provider_user_id, access_token, name, profile_url):
        self.email = email
        self.provider_id = provider_id
        self.provider_user_id = provider_user_id
        self.access_token = access_token
        self.name = name
        self.profile_url = profile_url
