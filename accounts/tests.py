from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class AccountsTest(TestCase):
    def test_we_can_create_user_in_model(self):
        get_user_model().objects.create_user(email='test@test.ok', password='123')

    def test_user_can_login(self):
        get_user_model().objects.create_user(email='test@test.ok', password='123')
        c = Client()
        response = c.post('/accounts/login/', {'email': 'test@test.ok', 'password': '123'})
        self.assertEqual(response.status_code, 302)

    def test_new_user_automatically_acquires_related_classes(self):
        user = get_user_model().objects.create_user(email='unit_test_user@test.ok', password='123')
        self.assertTrue(user.athlete is not None)
        self.assertTrue(user.workoutdiary is not None)
