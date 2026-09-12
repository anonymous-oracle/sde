# build a full python middle ware from scratch
# add a security middleware section
# add context management for middlewares, pre and post request execution specifically
import sys


class Middleware:
    def __init__(self):
        self.middlewares = []
        self.context = {}  # Context for middlewares

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)

    def execute(self, request):
        # Pre-request execution
        self.context['pre_request'] = True

        for middleware in self.middlewares:
            response = middleware(request, self.context)
            if response:
                return response

        # Post-request execution
        self.context['post_request'] = True

        return None

# Example usage
def middleware1(request, context):
    if request == "block":
        return "Blocked by middleware1"
    return None

def middleware2(request, context):
    if request == "allow":
        return "Allowed by middleware2"
    return None

# Security middleware
def security_middleware(request, context):
    if request == "unauthorized":
        return "Blocked by security middleware"
    return None

mw = Middleware()
mw.add_middleware(middleware1)
mw.add_middleware(middleware2)
mw.add_middleware(security_middleware)

request = "block"
response = mw.execute(request)
print(response)  # Output: Blocked by middleware1

request = "allow"
response = mw.execute(request)
print(response)  # Output: Allowed by middleware2

request = "unauthorized"
response = mw.execute(request)
print(response)  # Output: Blocked by security middleware

request = "other"
response = mw.execute(request)
print(response)  # Output: None