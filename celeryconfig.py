import urllib.parse

from kombu import Exchange, Queue
from decouple import config

aws_access_key_id=config('AWS_ACCESS_KEY_ID')
aws_secret_key=config('AWS_SECRET_KEY')

broker_url = 'sqs://{0}:{1}@'.format(
    urllib.parse.quote(aws_access_key_id, safe=''),
    urllib.parse.quote(aws_secret_key, safe='')
)

task_queues = (
    Queue(
        'test-celery',
        Exchange('test-celery')
    ),
)

if __name__ == '__main__':
    print(BROKER_URL)
