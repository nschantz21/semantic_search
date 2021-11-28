"""sem_search.py

Implementation of Semantic Search Algorithm
Author: Nicholas Schantz
"""
# imports
import os
from google.cloud import bigquery
from google.oauth2 import service_account
import json

# constants
AUTH_KEY = json.loads(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
credentials = service_account.Credentials.from_service_account_info(
    AUTH_KEY)

# functions
def semantic_search():
    """
    Semantic Search Algorithm
    """
    pass


client = bigquery.Client(credentials=credentials)

# Perform a query.
QUERY = (
    'SELECT name FROM `nwo-sample.graph.tweets` '
    'LIMIT 10')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)




