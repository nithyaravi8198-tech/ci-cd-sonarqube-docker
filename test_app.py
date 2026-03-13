import unittest
from app import hello

class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "CI/CD Jenkins Pipeline Triggered")

if __name__ == "__main__":
    unittest.main()
