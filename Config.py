


class Config(object):
    CELERY_BROKER_URL = "amqp://admin:qscan@localhost:5672/"
    # 快速扫描的端口
    QUICK_PORTS = [80,443]
