class PrException(Exception):
    """Exception class of FPF with message as a required parameter"""

    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


# example for the usage of PrException

# try:
#     raise PrException('This is a test')
# except PrException as e:
#     print(e.message)
