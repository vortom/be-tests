from common.test import E2eTest

def pytest_addoption(parser):
    E2eTest.addoption(parser)

def pytest_configure(config):
    E2eTest.configure(config)
