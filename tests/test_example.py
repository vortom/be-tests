from locust import task, between
from common.test import TestRunner


class TestSuiteExample(TestRunner):
    # Locust options and variables
    wait_time = between(1, 10)

    # General options and variables
    pets = {}
    
    @task()
    def test_case_example(self):
        # Add a new pet
        new_pet = self.services.pet.add_new_pet(json=self.tools.generate_pet_data(), headers=self.user.auth.header).json()
        pet_id = new_pet["id"]
        self.pets[pet_id] = new_pet
        # self.tools.test_sleep(1)

        # Find new pet by ID
        resp = self.services.pet.find_pet_by_id(pet_id, headers=self.user.auth.header)
        assert resp.json() == self.pets[pet_id]

        # # Delete the new pet by ID
        resp = self.services.pet.delete_pet_by_id(pet_id, headers=self.user.auth.header)
        assert resp.status_code == 200, f"Expected status code 200, but got {resp.status_code}"

        # Find the deleted pet by ID and check if it returns 404
        self.services.pet.find_pet_by_id(pet_id, headers=self.user.auth.header, expected_status_code=404)
        self.pets.pop(pet_id)
        self.logger.debug("Test failed sucefully")
