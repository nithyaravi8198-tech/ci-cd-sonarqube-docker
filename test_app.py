import unittest
from app import hello

class TestApp(unittest.TestCase):

        def test_hello(self):
                    self.assertEqual(1,1)

                    if __name__ == "__main__":
                            unittest.main()
