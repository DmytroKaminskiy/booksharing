from time import time


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        1. Create `model` (models.py) Log with fields
           - path (request.path)
           - method (request.method)
           - time (end - start)
        2. Disallow Author Delete
        """
        start = time()
        response = self.get_response(request)
        end = time()
        # print(f'Request-Response took: {end - start}')

        # Log.objects.create(...)
        return response
