def reddit_pipeline(file_name: str, subreddit: str, time_filter = 'day', limit = None):
    # conexão da instancia reddit
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholer Agent')
    # extração
    #transformação 
    #carregamento para CSV