from flask import Flask
import unittest
import json

from config import TestConfig
from main import hw, db, FactoryLog


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(TestConfig)
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def test_basic(self):
        with self.app.app_context():
            with self.app.test_request_context('/'):
                res = hw()
                self.assertEqual(res.status_code, 200)
                self.assertEqual(service_time(res), 0)

    def tearDown(self):
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()


def service_time(res):
    return json.loads(res.get_data(True))['AverageServiceTime']


if __name__ == '__main__':
    unittest.main()
