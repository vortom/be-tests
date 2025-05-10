from locust import FastHttpUser
from common.base_setup import BaseSetup
from common.test_services import TestServices
from common.test_tools import TestTools
from common.test_users import TestUsers
from os import environ
import tomllib

test_env = environ.get('BET_ENV')
assert test_env, "Env variable not set, e.g.: export BET_ENV=local"
test_type = environ.get("BET_TYPE")
assert test_type, "Test type variable not set, e.g.: export BET_TYPE=e2e"


class Env(BaseSetup):
    with open(f"./configs/{test_env}.toml", "rb") as f:
        config = tomllib.load(f)

    host = config["api"]["petstore"]["host"]
    api_key = config["api"]["petstore"]["api-key"]
    user_agent = config["test"]["common"]["user-agent"]
    username_prefix = config["test"]["common"]["username-prefix"]


class E2eTest(Env):
    @classmethod
    def setup_class(cls):
        cls.services = TestServices(cls.host, cls.user_agent)
        cls.tools = TestTools()
        cls.user = TestUsers(cls.tools.generate_username(cls.username_prefix), cls.api_key)
        cls.user.create()
        
    @classmethod
    def teardown_class(cls):
        cls.user.delete()

    def setup_method(self, method):
        self.user.refresh()

    def teardown_method(self, method):
        pass

    @classmethod
    def addoption(cls, parser):
        parser.addoption(
            "--argA", "-A",
            action="store", 
            required=False, 
            default="A",
            help="Arg A."
        )

        parser.addoption(
            "--argB", "-B",
            action="store", 
            required=False, 
            default="B",
            help="Arg B."
        )

    @classmethod
    def configure(cls, config):
        cls.option_config = config.getoption("argA")
        cls.option_example = config.getoption("argB")


class PerfTest(Env, FastHttpUser):
    abstract = True
    
    def __init__(self, environment):   
        super().__init__(environment)
        assert self.host == self.environment.host, f"Host mismatch: {self.host} != {self.environment.host}"
        self.services = TestServices(self.host, self.user_agent)
        for attr_name in dir(self.services):
            attr = getattr(self.services, attr_name)
            if hasattr(attr, "session"):
                attr.session = self.client
        self.tools = TestTools()
        self.user = TestUsers(self.tools.generate_username(self.username_prefix), self.api_key)
        self.user.create()

    def __del__(self):
        self.user.delete()


if test_type == "e2e":
    TestRunner = E2eTest
elif test_type == "perf":
    TestRunner = PerfTest
else:
    raise ValueError(f"Unknown test type: {test_type}")
