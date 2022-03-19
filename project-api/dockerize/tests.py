from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Dockerize

class DockerizeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_dockerize = Dockerize.objects.create(name='rake', owner=testuser1,description='Better for collecting leaves than a shovel.')
        test_dockerize.save()

    def test_dockerizes_model(self):
        dockerize = Dockerize.objects.get(id=1)
        actual_owner = str(dockerize.owner)
        actual_name = str(dockerize.name)
        actual_description = str(dockerize.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'rake')
        self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')