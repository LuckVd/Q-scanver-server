from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from common.schemas import UserSchema, TaskSchema
from utils.task_helper import submit_task

task_bp = Blueprint('task',__name__)


# base_search_task_fields = {
#     'name': fields.String(required=False, description="任务名"),
#     'target': fields.String(description="任务目标"),
#     'status': fields.String(description="任务状态"),
#     '_id': fields.String(description="任务ID"),
# }




@task_bp.route("/users", methods=["POST"])
def create_user():
    schema = UserSchema()
    try:
        data = schema.load(request.get_json())
        # 保存 data 到数据库
        return jsonify({"message": "User created"}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    schema = TaskSchema()
    try:
        task_data = schema.load(request.get_json())
        message = submit_task(task_data)
        return jsonify({"message": "Task created"}),201
    except ValidationError as err:
        return jsonify({"errors":err.messages}),400




