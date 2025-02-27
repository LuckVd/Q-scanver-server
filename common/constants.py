

class TaskTypes(object):
    COMMON_TASK = "common"


class CeleryRoutingKey:
    SCAN_TASK = "scan"


class TaskStatus:
    WAITING = "waiting"
    DONE = "done"
    ERROR = "error"
    STOP = "stop"