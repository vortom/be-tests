from common.base_setup import BaseSetup


class Auth():
    access_token = None
    refresh_token = None
    header = {"Authorization": f"Bearer {access_token}"}


class TestUsers(BaseSetup):
    def __init__(self, user_name: str, user_secret: str, user_id: str | None = None):
        self.user_name = user_name
        self.user_secret = user_secret
        self.user_id = user_id
        self.auth = Auth()

    def create(self):
        # TODO - implement the logic to create a user
        self.logger.info(f"Creating user {self.user_name}...")
        self.access_token = self.user_secret

    def delete(self):
        # TODO - implement the logic to delete user
        self.logger.info(f"Deleting user {self.user_name}...")
        self.access_token = None
        self.refresh_token = None

    def refresh(self):
        # TODO - implement the logic to refresh token
        self.logger.info(f"Refreshing user {self.user_name}...")
        self.access_token = self.user_secret





