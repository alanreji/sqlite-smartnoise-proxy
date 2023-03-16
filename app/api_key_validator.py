from app.configuration import Configuration


class ApiKeyValidator:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def validate(self):
        if self.api_key != Configuration().api_key:
            return False
        return True