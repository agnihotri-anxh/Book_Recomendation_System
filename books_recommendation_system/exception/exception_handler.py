class AppException(Exception):
    def __init__(self, message, sys_info=None):
        super().__init__(message)
        self.sys_info = sys_info
