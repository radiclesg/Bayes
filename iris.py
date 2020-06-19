import google.cloud
from google.cloud import bigquery

bq_client = bigquery.Client.from_service_account_json('C:/Users/jermi/OneDrive/ML/eighth-ridge-280804-7610c9e229ea.json')
dataset_ref = bq_client.dataset('trump_tweets')
dataset = bigquery.Dataset(dataset_ref)
dataset = bq_client.create_dataset(dataset)


table_ref = dataset.table('tweet_data')
job_config = bigquery.LoadJobConfig()
job_config.source_format = 'NEWLINE_DELIMITED_JSON'
job_config.autodetect = True
with open ('twitter_data_set.json', mode='rb') as datafile:
    job = bq_client.load_table_from_file(datafile, table_ref, job_config=job_config)
