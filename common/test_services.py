from api.pet import PetApi


class TestServices():
    def __init__(self, host: str, user_agent: str):
        self.pet = PetApi(host, {"User-Agent": user_agent})
