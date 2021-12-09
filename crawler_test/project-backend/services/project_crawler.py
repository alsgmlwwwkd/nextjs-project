import pdb
from services import ServiceMethodBase
from libs.sql_manager import execute_sql_query

class ProjectCrawler(ServiceMethodBase):
    def __init__(self):
        super().__init__()

    def process(self, event):

        query = f'''
            select title, summary
            from crawler_test
        '''

        results = execute_sql_query(query)

        return results
    

def main(event, context):
    return ProjectCrawler.run(event, context)