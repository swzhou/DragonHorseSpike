import unittest

import requests_mock

import portal
import motor


class PortalTestCase(unittest.TestCase):

    def setUp(self):
        self.app = portal.app.test_client()

    def test_health(self):
        response = self.app.get("/health")
        assert b'alive' in response.data

    def test_pull(self):
        with requests_mock.mock() as m:
            duration = 5
            url = "http://{0}/pull/{1}".format(motor.SERVER_NAME, duration)
            expected_response = {"action": "pull", "status": "whatever", "duration": duration}
            m.get(url, json=expected_response)

            response = self.app.get("/pull/{0}".format(duration))

            assert b'whatever' in response.data