class R:
    def __init__(self, code: int, success: bool, message: str, data: object = None):
        self.code = code        # HTTP状态码或自定义业务码
        self.success = success  # 布尔类型表示成功/失败
        self.message = message  # 返回的提示信息
        self.data = data        # 可选的实际返回数据（泛型）

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "success": self.success,
            "message": self.message,
            "data": self.data
        }


    