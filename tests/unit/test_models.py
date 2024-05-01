from app.models.user import UserModel
from app.models.subscription import SubscriptionModel

def test_user_model():
    # Create a user instance
    user = UserModel(username='john_doe', email='john@example.com', password='password')

    # Test the attributes of the user instance
    assert user.username == 'john_doe'
    assert user.email == 'john@example.com'
    assert user.password == 'password'

def test_subscription_model():
    # Create a subscription instance
    subscription = SubscriptionModel(user_id=1, industry='Finance', source='Bloomberg', subcategory='Latest')

    # Test the attributes of the subscription instance
    assert subscription.user_id == 1
    assert subscription.industry == 'Finance'
    assert subscription.source == 'Bloomberg'
    assert subscription.subcategory == 'Latest'
