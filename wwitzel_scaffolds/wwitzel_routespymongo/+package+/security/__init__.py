from pyramid.security import (
    Allow,
    Everyone,
    ALL_PERMISSIONS,
)

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

class RootACL(object):
    __acl__ = [
        (Allow, Everyone, ALL_PERMISSIONS)
    ]

    def __init__(self, request):
        self.request = request

def groupfinder(userid, request):
    """Implement your groupfinder here. This should turn a list of
    groups for a given user.

    user = request.db.user.find_one({'user':userid})
    if user:
        return user.get('groups')
    """
    return []

def includeme(config):
    authn_policy = AuthTktAuthenticationPolicy(
        config.registry.settings['auth.secret'],
        callback=groupfinder,
    )
    authz_policy = ACLAuthorizationPolicy()

    config.set_authorization_policy(authz_policy)
    config.set_authentication_policy(authn_policy)
