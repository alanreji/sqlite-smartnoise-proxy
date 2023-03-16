from snsql.sql.private_reader import PrivateReader

class PrivateQueryRunner:
    @staticmethod
    def run_query(query, reader: PrivateReader):
        """Runs the query using the SmartNoise reader."""
        try:
            result = reader.execute(query)
            privacy_used = reader.odometer.spent
            return {'result': result, 'total_privacy_used': privacy_used}, 200
        except Exception as e:
            return {'query error': str(e)}, 500
