from common.base_setup import BaseSetup
import time
import uuid


class TestTools(BaseSetup):
    @classmethod
    def test_sleep(cls, seconds: int = 1):
        cls.logger.debug(f"Sleep test: {seconds}...")
        time.sleep(seconds)
    
    @classmethod
    def generate_pet_data(cls):
        return {
            "id": None,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
        }
    
    @classmethod
    def generate_username(cls, username_prefix: str):
        return f"{username_prefix}{uuid.uuid4().hex}"
