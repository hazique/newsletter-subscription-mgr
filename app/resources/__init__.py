from .subscription import SubscriptionResource

def initialize_routes(api):
#  api.add_resource(SubscriptionResource, '/subscription/<user_id>')
 api.add_resource(SubscriptionResource, '/subscription')
#  api.add_resource(MovieApi, '/movies/<id>')