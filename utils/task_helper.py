# id = fields.Int(dump_only=True)
# name = fields.Str(required=True)
# target = fields.List(fields.Str(), required=True)
# task_options = fields.Nested(Task_Options, required=True)
from common.constants import TaskTypes, TaskStatus

import utils.logger
from utils import task_delay
from utils.domain import valid_target_list

logger = utils.logger.get_logger()


def build_task(task_data):
    task_data = {
        'name': task_data["name"],
        'start_time': '-',
        'status': TaskStatus.WAITING,
        'type': task_data["type"],
        'options': task_data["task_options"],
        "end_time": "-",
        "celery_id": ""
    }

    return task_data


def submit_task(task_data):
    # 进行参数合理性校验
    if task_data["type"] == TaskTypes.COMMON_TASK:
        target_list = task_data["task_options"]["target"]
        #在这里进行target的合法性校验
        valid_list = valid_target_list(target_list)

        if target_list and valid_list:
            print(build_task(task_data))
            result = utils.task_delay.scan_task.delay(build_task(valid_list))
            print(result)
        else:
            return




    else:
        logger.error("Unknown task type")



