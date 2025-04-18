class ResponseFormat:
    @staticmethod
    def success(data: dict = None):
        return {
            "success": True,
            "data": data or {},
            "error": {
                "code": "",
                "message": "",
                "details": {}
            }
        }

    @staticmethod
    def error(code: str, message: str, details: dict = None):
        return {
            "success": False,
            "data": {},
            "error": {
                "code": code,
                "message": message,
                "details": details or {}
            }
        }
