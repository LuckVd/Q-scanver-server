from marshmallow import Schema, fields, validate, ValidationError, validates_schema

import utils.logger
from common import constants
from common.constants import TaskTypes

logger = utils.logger.get_logger()

valid_task_types = [value for key, value in vars(TaskTypes).items() if not key.startswith("__")]

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    role = fields.Str(validate=validate.OneOf(["admin", "user"]))

class PostSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Nested(UserSchema)  # 嵌套其他 Schema


class Common_Options(Schema):
    target = fields.List(fields.Str(), required=True)
    portscan_switch = fields.Bool(missing=False)
    portscan_type = fields.Str(validate=validate.OneOf(["all","quick","specify"]), missing="")
    server_switch = fields.Bool(missing=False)
    os_switch = fields.Bool(missing=False)


class DynamicNested(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if not isinstance(value, dict):
            raise ValidationError("Invalid nested data")

        type_value = data.get("type")
        if type_value == TaskTypes.COMMON_TASK:
            schema = Common_Options()
        elif type_value == TaskTypes.COMMON_TASK:
            schema = Common_Options()
        else:
            raise ValidationError(f"Unknown type: {type_value}")

        return schema.load(value)




class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(validate=validate.OneOf(valid_task_types))
    task_options = DynamicNested(required=True)










