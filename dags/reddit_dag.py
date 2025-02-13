from airflow import DAG
from datetime import datetime
import os
import sys

sys.path.insert(_index:0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Ray'
    'start_date': datetime(year: 2025, month:2, day:12)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline', 
    default_args = default_args,
    schedule_interval = '@daily'
    catchup = False, 
    tags = ['reddit', 'etl', 'pipeline']
)

#extração reddit
extract = PythonOperator(
    task_id = 'reddit_pipeline', 
    python_callable = reddit_pipeline,
    op_kwargs = {
        'file_name': f'reddit_{file_postfix}', 
        'subreddit'> 'dataengeneeirng',
        'time_filter': 'day', 
        'limit': 100
    }
)

#upload para o S3