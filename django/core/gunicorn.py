import os
import multiprocessing


bind = '0.0.0.0:8000'
workers = int(os.getenv('GUNICORN_WORKERS', multiprocessing.cpu_count()))
threads = int(os.getenv('GUNICORN_THREADS'), 1)
accesslog = 'logs/gunicorn_access.log'
errorlog = 'logs/gunicorn_error.log'
