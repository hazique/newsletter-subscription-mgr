from app.models import db
from app.models.user import UserModel
from app.models.subscription import SubscriptionModel

# from app.main import app
from app.models import db
import os

def load_data(app):
    
    db.init_app(app)
    with app.app_context():           
        if not is_db_present(app):
            db.create_all()
            user_ids = load_users()
            load_subscriptions(user_ids)

def load_users():
    users = [
        {
            'username': 'tim',
            'email': 'tim@email.com',
            'password': '9Jkp7d4F2GhR3sLt'
        },
        {
            'username': 'joe',
            'email': 'joe@email.com',
            'password': 'E4hWt9sP2mN6qA7j'
        }
    ]

    user_ids = []
    

    for user in users:
        user = UserModel(**user)
        user.save_to_db()
        user_ids.append(user.id)

    return user_ids


def load_subscriptions(user_ids):
    subscriptions = [
        {
            'user_id': 1,
            'industry': 'technology',
            'source': 'techcrunch',
            'subcategory': 'latest'
        },
        {
            'user_id': 2,
            'industry': 'technology',
            'source': 'techcrunch',
            'subcategory': 'latest'
        }
    ]

    for subscription, user_id in zip(subscriptions, user_ids):
        subscription['user_id'] = user_id
        subscription = SubscriptionModel(**subscription)
        subscription.save_to_db()

def is_db_present(app):
    db_path = os.path.join(app.instance_path, 'app.db')
    print("DB Path: ", db_path)
    return os.path.isfile(db_path)

    