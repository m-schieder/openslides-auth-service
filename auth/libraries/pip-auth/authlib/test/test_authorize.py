from .base import BaseTestEnvironment

from ..config import Environment
from ..constants import AUTHORIZATION_HEADER

class TestAuthorize(BaseTestEnvironment):
    environment = Environment()
    example_email = "maxmustermann@example.com"

    def test_create_authorize(self):
        response = self.auth_handler.create_authorization_token(1, self.example_email)
        token = response.headers.get(AUTHORIZATION_HEADER, "")
        self.assertTrue(response.ok)
        self.assertEqual("bearer ", token[0:7])

    def test_verify_authorize(self):
        response = self.auth_handler.create_authorization_token(1, self.example_email)
        user_id, email = self.auth_handler.verify_authorization_token(response.headers.get(AUTHORIZATION_HEADER, ""))
        self.assertEqual(user_id, 1)
        self.assertEqual(email, self.example_email)