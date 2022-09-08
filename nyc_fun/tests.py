from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import ToDo


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='pass')
        test_user.save()

        test_thing = ToDo.objects.create(author=test_user, thing_to_do="Go to a park", task_description="People Watch")
        test_thing.save()

    def test_things_model(self):
        thing = ToDo.objects.get(id=1)
        actual_author = str(thing.author)
        actual_thing_to_do = str(thing.thing_to_do)
        actual_task_description = str(thing.task_description)
        self.assertEqual(actual_author, "test_user")
        self.assertEqual(actual_thing_to_do, "Go to a park")
        self.assertEqual(actual_task_description, "People Watch")
