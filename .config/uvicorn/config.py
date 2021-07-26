bind = "unix:/tmp/uvicorn.sock"
wsgi_app = "config.wsgi:application"
backlog = 2048
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
reload = True
timeout = 30
keepalive = 3
spew = False
daemon = False
pidfile = None
umask = 0
user = "deploy"
group = "deploy"
tmp_upload_dir = None
logger_class = 'uvicorn.logger'
accesslog = "/var/log/uvicorn/access.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = "/var/log/uvicorn/error.log"
loglevel = "debug"
proc_name = None