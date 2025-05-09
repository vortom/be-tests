from common.base_setup import BaseSetup
import requests


class HttpClient(BaseSetup):
    def __init__(self, cert: str | None = None):
        self.cert = cert
        self.session = requests.sessions.Session()
        # self.session.headers.update({"User-Agent": self.user_agent})
        
    def rest(self, method, url, headers, params, data, json, name: str | None = None, expected_status_code: int | None = None):
        request_id = self.random_string()
        
        self.logger.info(f"<{request_id}> Request started {method} {url}")
        self.logger.debug(f"<{request_id}> Request headers: {headers}")
        self.logger.debug(f"<{request_id}> Request params: {params}")
        self.logger.debug(f"<{request_id}> Request data: {data}")
        self.logger.debug(f"<{request_id}> Request json: {json}")

        if isinstance(self.session, requests.sessions.Session):
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    data=data,
                    json=json,
                    cert=self.cert
                )

                if expected_status_code:
                    assert response.status_code == expected_status_code, f"Unexpected status code {response.status_code}, expected {expected_status_code} | request_id {request_id}"

                else:
                    response.raise_for_status()

            except requests.exceptions.RequestException as e:
                self.logger.error(f"<{request_id}> Request failed: {e}")
                raise

        else:
            catch_response = False
            if expected_status_code:
                catch_response = True

            with self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                cert=self.cert,
                name=name,
                catch_response=catch_response
            ) as response:
                if catch_response and response.status_code == expected_status_code:
                        response.success()
                elif catch_response and response.status_code != expected_status_code:
                        self.logger.error(f"<{request_id}> Unexpected status code {response.status_code}, expected {expected_status_code} | request_id {request_id}")
                        response.failure(f"Unexpected status code {response.status_code}, expected {expected_status_code}")

        self.logger.info(f"<{request_id}> Request finished with status code {response.status_code}")
        self.logger.debug(f"Response headers: {response.headers}")
        self.logger.debug(f"Response body: {response.text.replace("\n", "") if response.text else 'No Content'}")
        
        return response
