from prometheus_client import Gauge, start_http_server

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.3; charset=utf-8')

############ Generate Metrics ############
GARBAGE_HEIGHT_METRIC = Gauge('garbage_height', 'The height of the trash inside the trash can')
