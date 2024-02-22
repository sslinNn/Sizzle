from django.test import TestCase


class TestUsers(TestCase):
    def test_users_login(self):
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 200)

    def test_users_register(self):
        response = self.client.get('/user/register/')
        self.assertEqual(response.status_code, 200)
