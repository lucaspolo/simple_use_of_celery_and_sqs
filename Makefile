run-workers:
	celery -A tasks worker --loglevel=info
run-beat:
	celery -A tasks beat --loglevel=info
