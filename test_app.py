import unittest
from app import hello

class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello from CI/CD Pipeline with Jenkins + SonarQube + Docker!")

if __name__ == "__main__":
    unittest.main()
