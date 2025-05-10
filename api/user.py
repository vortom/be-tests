from common.http_client import HttpClient
from urllib.parse import urljoin


class UserApi(HttpClient):
    # https://petstore.swagger.io/#/user/

    def __init__(self, host: str | None, headers: dict | None = None):
        super().__init__()
        self.host = host
        self.headers = headers or {}

    def get_user_by_name(self, username: str, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/user/getUserByName
        endpoint = f"/v2/user/{username}"

        return self.rest(
            method="GET",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            name=endpoint,
            expected_status_code=expected_status_code
        )

    def update_user(self, username: str, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/user/updateUser
        endpoint = f"/v2/user/{username}"

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

    def delete_user(self, username: str, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/user/deleteUser
        endpoint = f"/v2/user/{username}"

        return self.rest(
            method="DELETE",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            name=endpoint,
            expected_status_code=expected_status_code
        )
