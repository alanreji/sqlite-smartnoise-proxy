import re

def validate_query(query, allowed_queries):
    for pattern in allowed_queries:
        if re.match(pattern, query):
            return True
    return False
