from django.apps import apps
from django.test import TestCase
from django.apps import AppConfig
from .apps import TodoConfig

class TestTodoConfig(TestCase):
    def test_app(self):
        self.assertEqual("todo", TodoConfig.name)
        self.assertEqual("<AppConfig: todo>", str(apps.get_app_config("todo")))
