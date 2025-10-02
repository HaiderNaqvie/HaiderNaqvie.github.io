import multiprocessing

bind = "0.0.0.0:8000"
workers = max(2, multiprocessing.cpu_count() * 2 + 1)
worker_class = "gthread"
threads = 2
preload_app = True
accesslog = "-"
errorlog = "-"
