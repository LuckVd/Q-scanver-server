import time

from celery import Celery, current_task
import signal
from Config import Config
from common.constants import CeleryRoutingKey, TaskTypes
from utils.logger import get_logger

logger = get_logger()

def create_celery_app():
    celery = Celery('task', broker=Config.CELERY_BROKER_URL)

    celery.conf.update(
        task_acks_late=False,
        worker_prefetch_multiplier=1,
        broker_transport_options={"max_retries": 3, "interval_start": 0, "interval_step": 0.2, "interval_max": 0.5},
    )

    return celery

celery = create_celery_app()


@celery.task(queue=CeleryRoutingKey.SCAN_TASK)
def scan_task(task_data):
    # 这里不检验 celery_action， 调用的时候区分
    run_task(task_data)




def run_task(task_data):
    signal.signal(signal.SIGTERM, sigterm_handler)
    action = task_data.get("celery_action")
    data = task_data.get("data")
    action_map = {
        TaskTypes.COMMON_TASK: common_task,
    }
    start_time = time.time()
    # 这里监控任务 task_id 和 target 是空的
    logger.info("run_task action:{} time: {}".format(action, start_time))
    logger.info("name:{}, target:{}, task_id:{}".format(
        data.get("name"), data.get("target"), data.get("task_id")))
    try:
        fun = action_map.get(action)
        if fun:
            fun(data)
        else:
            logger.warning("not found {} action".format(action))
    except Exception as e:
        logger.exception(e)

    elapsed = time.time() - start_time
    logger.info("end {} elapsed: {}".format(action, elapsed))




def sigterm_handler(signum, frame):
    if not current_task:
        return


def common_task(options):
    1
