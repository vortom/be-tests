from common.http_client import HttpClient
from urllib.parse import urljoin


class PetApi(HttpClient):
    # https://petstore.swagger.io/#/pet/

    def __init__(self, host: str | None, headers: dict | None = None):
        super().__init__()
        self.host = host
        self.headers = headers or {}

    def find_pet_by_id(self, pet_id: int, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/pet/getPetById   
        endpoint = f"/v2/pet"

        return self.rest(
            method="GET",
            url=urljoin(self.host, f"{endpoint}/{pet_id}"),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            data=kwargs.get("data", None),
            json=kwargs.get("json", {}),
            name=endpoint,
            expected_status_code=expected_status_code
        )
    
    def add_new_pet(self, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/pet/addPet
        endpoint = "/v2/pet"

        return self.rest(
            method="POST",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            data=kwargs.get("data", None),
            json=kwargs.get("json", {}),
            name=endpoint,
            expected_status_code=expected_status_code
        )
    
    def delete_pet_by_id(self, pet_id: int, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/pet/deletePet
        endpoint = f"/v2/pet"

        return self.rest(
            method="DELETE",
            url=urljoin(self.host, f"{endpoint}/{pet_id}"),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            data=kwargs.get("data", None),
            json=kwargs.get("json", {}),
            name=endpoint,
            expected_status_code=expected_status_code
        )
