from services import ServiceMethodBase
from libs.sql_manager import execute_sql_query

class FredSeriesValues(ServiceMethodBase):
    def __init__(self):
        super().__init__()

    def process(self, event):
        # not killed
        params = event.get('queryStringParameters', None)

        # exception for debugging
        if params is None:
            raise RuntimeError("Query string parameter is missing")

        series_id = params.get('series_id', None)

        if series_id is None:
            raise RuntimeError(
                "series_id is missing from query string parameters"
            )

        query = f'''
            select date, value
            from fred_series_values
            where series_id = '{series_id}' and value is not null
        '''
        

        results = execute_sql_query(query)

        return results
    

def main(event, context):
    return FredSeriesValues.run(event, context)