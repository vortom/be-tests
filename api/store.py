from common.http_client import HttpClient
from urllib.parse import urljoin


class StoreApi(HttpClient):
    # https://petstore.swagger.io/#/store/

    def __init__(self, host: str | None, headers: dict | None = None):
        super().__init__()
        self.host = host
        self.headers = headers or {}

    def get_inventory(self, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/store/getInventory
        endpoint = "/v2/store/inventory"

        return self.rest(
            method="GET",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            name=endpoint,
            expected_status_code=expected_status_code
        )

    def place_order(self, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/store/placeOrder
        endpoint = "/v2/store/order"

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

    def get_order_by_id(self, order_id: int, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/store/getOrderById
        endpoint = f"/v2/store/order/{order_id}"

        return self.rest(
            method="GET",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            name=endpoint,
            expected_status_code=expected_status_code
        )

    def delete_order(self, order_id: int, expected_status_code: int = 200, **kwargs):
        # https://petstore.swagger.io/#/store/deleteOrder
        endpoint = f"/v2/store/order/{order_id}"

        return self.rest(
            method="DELETE",
            url=urljoin(self.host, endpoint),
            headers={**kwargs.get("headers", {}), **self.headers},
            params=kwargs.get("params", []),
            name=endpoint,
            expected_status_code=expected_status_code
        )
