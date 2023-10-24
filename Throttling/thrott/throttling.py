from rest_framework.throttling import UserRateThrottle

class JackThrottel(UserRateThrottle):
    scope = 'jack'