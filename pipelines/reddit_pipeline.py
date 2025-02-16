from elts.reddit_etl import connect_reddit
from utils.constants import CLIEND_ID, SECRET

def reddit_pipeline(file_name: str, subreddit: str, time_filter = 'day', limit = None):
    # conexão da instancia reddit
    instance = connect_reddit(CLIENT_ID, SECRET, user_agent: 'Airscholer Agent')

    # extração
    posts = extract_posts(instance, subreddit, time_filter, limit)
    #transformação 

    #carregamento para CSV
