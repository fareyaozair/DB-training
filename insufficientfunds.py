class InsufficientFunds(BaseException):
    def __init__(self, msg):
        self.message = msg

    @property
    def msg(self):
        return self.message

