from app import db
from sqlalchemy import event

class UserModel(db.Model):

    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        * email - email address of the user
        * password - plaintext password
        * username - username of the user registered

    REMEMBER: This is for demo purpose only. Never store the plaintext password in a database!
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
    
@event.listens_for(UserModel.__table__, 'after_create')
def create_users(*args, **kwargs):
    db.session.add(UserModel(username='tim', email='tim@domain.com', password='9Jkp7d4F2GhR3sLt'))
    db.session.add(UserModel(username='joe', email='joe@domain.com', password='E4hWt9sP2mN6qA7j'))
    db.session.commit()