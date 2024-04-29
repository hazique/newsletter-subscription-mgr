# resources.py
from flask import request
from flask_restful import Resource
from ..models.subscription import SubscriptionModel

class SubscriptionResource(Resource):
    def post(self):
        data = request.get_json()
        # Validate data
        existing_subscription = SubscriptionModel.find_by_user_id(data.get('user_id'))
        if existing_subscription:
            return {'message': 'Subscription exists'}, 409
        new_subscription = SubscriptionModel(**data)
        new_subscription.save_to_db()
        return {'message': 'Subscription created successfully'}, 201

    def get(self):
        user_id = request.get_json().get('user_id')
        subscription = SubscriptionModel.find_by_user_id(user_id)
        if subscription:
            return subscription.json()
        return {'message': 'Subscription not found'}, 404

    def put(self):
        data = request.get_json()
        user_id = data.get('user_id')
        if 'user_id' in data:
            del data['user_id']
        subscription = SubscriptionModel.find_by_user_id(user_id)
        if subscription:
            subscription.update(**data)
            return {'message': 'Subscription updated successfully'}, 200
        return {'message': 'Subscription not found'}, 404

    def delete(self):
        user_id = request.get_json().get('user_id')
        subscription = SubscriptionModel.find_by_user_id(user_id)
        if subscription:
            subscription.delete_from_db()
            return {'message': 'Subscription deleted successfully'}, 200
        return {'message': 'Subscription not found'}, 404
