from django.test import Client, TestCase

from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ['test_users.json']

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.get(id=1)
        self.user2 = User.objects.get(id=2)

        self.user_count = User.objects.count()

        self.valid_user_data = {
            'first_name': 'Monica',
            'last_name': 'Geller',
            'username': 'shef',
            'password1': 'garlic',
            'password2': 'garlic'
        }

        self.update_user_data = {
            'first_name': 'Chandler',
            'last_name': 'Bing',
            'username': 'Sharks',
            'password1': 'NewPass',
            'password2': 'NewPass'
        }
