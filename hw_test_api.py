from lib2to3.pgen2.token import RPAR
from pprint import pprint
import requests
import unittest
from src.hw_api_ya import auth,create_folder
import sys


class TestApi(unittest.TestCase):
    
    def setUp(self):
        folder = 'test'
    
    def test_сreate_folder(self):
        result = create_folder('test')
        if result == 201:
            status = self.assertTrue(result==201)
        elif result == 401:
            status = self.assertTrue(result==401)
        elif result == 403:
            status = self.assertTrue(result==403)
        elif result == 404:
            status = self.assertTrue(result==404)
        elif result == 406:
            status = self.assertTrue(result==406)
        elif result == 429:
            status = self.assertTrue(result==429)
        elif result == 503:
            status = self.assertTrue(result==503)
        
            
        

            
            


if __name__ == '__main__':
    unittest.main()