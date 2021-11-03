import pdb

from services import ServiceMethodBase
from libs.sql_manager import execute_sql_query

class FredSeriesList(ServiceMethodBase):
    def __init__(self):
        super().__init__()

    def process(self, event):
        query = """
            select series_id, title, observation_start, observation_end
            from fred_series_info
        """

        results = execute_sql_query(query)

        return results
        

def main(event, context):
    return FredSeriesList.run(event, context)