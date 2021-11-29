"""sem_search.py

Implementation of Semantic Search Algorithm
Author: Nicholas Schantz
"""
# imports
import os
from google.cloud import bigquery
from google.oauth2 import service_account
import json
import sentence_transformers

# constants
AUTH_KEY = json.loads(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
credentials = service_account.Credentials.from_service_account_info(AUTH_KEY)

TWITTER_DB_NAME = "nwo-sample.graph.tweets"
REDDIT_DB_NAME = "nwo-sample.graph.reddit"


# functions
def semantic_search():
    """
    Semantic Search Algorithm
    """
    pass


client = bigquery.Client(credentials=credentials)

# Perform a query.
QUERY = ('SELECT * FROM `{}` LIMIT 10'.format(REDDIT_DB_NAME))
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row)
