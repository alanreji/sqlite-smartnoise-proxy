import json

from snsql import Privacy

from app.db_connector import DBConnector


class Configuration:
    def __init__(self):
        self._config = json.load(open('config/config.json'))

    @property
    def allowed_sql_functions(self):
        return self._config['allowed_sql_functions']

    @property
    def privacy(self):
        return Privacy(epsilon=self._config['epsilon'], delta=self._config['delta'])
    
    @property
    def api_key(self):
        return self._config['api_key']