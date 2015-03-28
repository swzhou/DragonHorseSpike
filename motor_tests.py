import unittest
import motor


class MotorTestCase(unittest.TestCase):

    def setUp(self):
        motor.app.config['USE_REAL_SERIAL'] = False
        self.app = motor.app.test_client()

    def test_pull(self):
        duration = 5
        response = self.app.get("/pull/{0}".format(duration))
        print(response.data)
        assert b'{\n  "action": "pull",\n  "duration": "5",\n  "status": "success"\n}' in response.data

if __name__ == '__main__':
    unittest.main()