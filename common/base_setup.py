import logging
import random
import string


class BaseSetup():
    logger = logging.getLogger("be-tests")
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    @classmethod
    def random_string(cls, length: int = 8):
        alphabet = string.ascii_lowercase + string.digits
        return "".join(random.choices(alphabet, k=length))
