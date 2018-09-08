from flask import Flask, json, Response

class ApiResult(object):
    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value),
                        status=self.status,
                        mimetype='application/json')

class ApiFlask(Flask):

    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)

class ApiException(object):
    def __init__(self, message, status=400):
        self.message=message
        self.status = status

    def to_result(self):
        return ApiResult({'message': self.message},
                         status=self.status)

