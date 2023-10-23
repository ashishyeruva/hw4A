"""
Name: Ashish Reddy Yeruva
Cwid:20012794
Subject: SSW - 567 WS
HW 04a Homework 04a
"""
import unittest
from unittest.mock import patch
from getRepo import getRepo

class TestGithubAPI(unittest.TestCase):
    @patch('getRepo.requests.get')
    def testGithub1(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value ={
            "login": "ashishreddy28"
        }

        result = getRepo('ashishreddy28')

        self.assertTrue(result)

if _name_ == '_main_':
    print('Running unit tests')
    unittest.main()
