import json
import decimal
import datetime


class DefaultEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal): # Decimal encoders
            return str(o)
        elif isinstance(o, datetime.date): # Datetime encoders
            return str(o)
        else:
            return o