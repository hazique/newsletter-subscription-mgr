import pytest
# from app.resources.subscription import SubscriptionResource


def test_get_subscription_not_found(test_client):
    # Test getting a non-existing subscription
    # Use the subscription_resource fixture to access the SubscriptionResource instance
    # Perform the necessary assertions to verify the behavior
    response = test_client.get('/subscription', json={'user_id': 3})
    assert response.status_code == 404
    assert response.json == {'message': 'Subscription not found'}

def test_get_subscription(test_client):
    # Test getting an existing subscription
    # Use the subscription_resource fixture to access the SubscriptionResource instance
    # Perform the necessary assertions to verify the behavior
    response = test_client.get('/subscription', json={'user_id': 1})
    assert response.status_code == 200
    assert response.json == {'user_id': 1, 'industry': 'Technology', 'source': 'TechCrunch', 'subcategory': 'Latest'}

def test_delete_subscription(test_client):
    # Test deleting an existing subscription
    # Use the subscription_resource fixture to access the SubscriptionResource instance
    # Perform the necessary assertions to verify the behavior
    response = test_client.delete('/subscription', json={'user_id': 2})
    assert response.status_code == 200
    assert response.json == {'message': 'Subscription deleted successfully'}

def test_create_subscription(test_client):
    # Test creating a new subscription
    # Use the subscription_resource fixture to access the SubscriptionResource instance
    # Perform the necessary assertions to verify the behavior
    response = test_client.post('/subscription', json={'user_id': 2, 'industry': 'Finance', 'source': 'Bloomberg', 'subcategory': 'Latest'})
    assert response.status_code == 201
    assert response.json == {'message': 'Subscription created successfully'}


def test_update_subscription(test_client):
    # Test updating an existing subscription
    # Use the subscription_resource fixture to access the SubscriptionResource instance
    # Perform the necessary assertions to verify the behavior
    response = test_client.put('/subscription', json={'user_id': 2, 'industry': 'Technology', 'source': 'TechCrunch', 'subcategory': 'Latest'})
    assert response.status_code == 200
    assert response.json == {'message': 'Subscription updated successfully'}



