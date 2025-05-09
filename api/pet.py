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

    def upload_pet_image(self, pet_id: int, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/pet/uploadFile
        endpoint = f"/v2/pet/{pet_id}/uploadImage"

        return self.rest(
            method="POST",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            data=kwargs.get("data", None),
            files=kwargs.get("files", None),
            name=endpoint,
            expected_status_code=expected_status_code
        )

    def update_pet(self, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/pet/updatePet
        endpoint = "/v2/pet"

        return self.rest(
            method="PUT",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            data=kwargs.get("data", None),
            json=kwargs.get("json", {}),
            name=endpoint,
            expected_status_code=expected_status_code
        )

    def find_pets_by_status(self, status: list[str], expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/pet/findPetsByStatus
        endpoint = "/v2/pet/findByStatus"

        return self.rest(
            method="GET",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params={"status": status},
            name=endpoint,
            expected_status_code=expected_status_code
        )

    def update_pet_with_form(self, pet_id: int, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/pet/updatePetWithForm
        endpoint = f"/v2/pet/{pet_id}"

        return self.rest(
            method="POST",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            data=kwargs.get("data", {}),
            name=endpoint,
            expected_status_code=expected_status_code
        )
