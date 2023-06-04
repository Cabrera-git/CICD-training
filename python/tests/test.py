import unittest
from functions import app
import sys
sys.path.append('../functions')

class FuncTest(unittest.TestCase):
    def handler(self):
        result = app.lambda_handler(None, None)
        self.assertEqual(result, "response")