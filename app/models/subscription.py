from sqlalchemy import event
from app import db

class SubscriptionModel(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    subcategory = db.Column(db.String(100), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('subscriptions', lazy=True))

    def __init__(self, user_id, industry, source, subcategory):
        self.user_id = user_id
        self.industry = industry
        self.source = source
        self.subcategory = subcategory

    def json(self):
        return {
            'user_id': self.user_id,
            'industry': self.industry,
            'source': self.source,
            'subcategory': self.subcategory
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update(self, industry, source, subcategory):
        self.industry = industry
        self.source = source
        self.subcategory = subcategory
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

@event.listens_for(SubscriptionModel.__table__, 'after_create')
def create_subscriptions(*args, **kwargs):
    db.session.add(SubscriptionModel(user_id=1, industry='Technology', source='TechCrunch', subcategory='Latest'))
    db.session.add(SubscriptionModel(user_id=2, industry='Technology', source='TechCrunch', subcategory='Latest'))  
    db.session.commit()