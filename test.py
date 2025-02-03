import unittest
from extract import extract_cookies

class TestCookieExtraction(unittest.TestCase):
    def test_extraction(self):
        cookies = extract_cookies("chrome")
        self.assertIsNotNone(cookies)
        self.assertTrue("name" in cookies.columns)

if __name__ == '__main__':
    unittest.main()
