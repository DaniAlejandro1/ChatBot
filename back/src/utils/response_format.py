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

    @staticmethod
    def success_uf(data: dict = None):
        return {
        "success": True,
        "data": data or {},
        "error": {
            "detail": ""
        }
    }

    @staticmethod
    def success_dolar(data: dict = None):
        return {
        "success": True,
        "data": data or {},
        "error": {
            "detail": ""
        }
    }

    @staticmethod
    def success_noticias(data: dict = None):
        return {
        "success": True,
        "data": data or {},
        "error": {
            "detail": ""
        }
    }

    @staticmethod
    def error_personalizado():
        return {
            "error": {
                "details": "En estos momentos no puedo mostrarte la información solicitada :("
            }
        }


