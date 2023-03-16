import sqlparse

def validate_query(query, supported_functions):
    parsed = sqlparse.parse(query)[0]

    for token in parsed.tokens:
        if isinstance(token, sqlparse.sql.Function):
            for function in supported_functions:
                if function in token.normalized:
                    return True
    return False
