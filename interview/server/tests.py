import requests
import unittest
import random
from random import randint
from datetime import datetime 
random.seed(datetime.now())

class TestStringMethods(unittest.TestCase):
    def test_get(self):
        response = requests.get('http://127.0.0.1:8000/conversations/1234')
        self.assertIn("anson", response.text)
    
    def test_get_non_existent(self):
        response = requests.get('http://127.0.0.1:8000/conversations/12456')
        self.assertIn("matching query does not exist", response.text)
    
    def test_get_non_int(self):
        response = requests.get('http://127.0.0.1:8000/conversations/124abc')
        self.assertEqual(response.status_code, 404)
    
    def test_get_nothing(self):
        response = requests.get('http://127.0.0.1:8000/conversations/')
        self.assertEqual(response.status_code, 404)
    
    def test_post(self):
        rand_int = str(randint(1000,9999))
        data = {"id": rand_int ,"sender": "anson", "message": "I am a coffee pot" }
        response = requests.post('http://127.0.0.1:8000/messages/', json=data)
        self.assertIn("Successfully stored", response.text)
        response = requests.get('http://127.0.0.1:8000/conversations/'+rand_int)
        self.assertIn("anson", response.text)
    
    def test_post_no_id(self):
        data = {"sender": "anson", "message": "I am a coffee pot"}
        response = requests.post('http://127.0.0.1:8000/messages/', json=data)
        self.assertIn("error", response.text)
    
    def test_post_no_sender(self):
        data = {"id": "12", "message": "I am a coffee pot"}
        response = requests.post('http://127.0.0.1:8000/messages/', json=data)
        self.assertIn("error", response.text)
    
    def test_post_no_message(self):
        data = {"id": "12", "sender": "raj", "message": "I am a coffee pot"}
        response = requests.post('http://127.0.0.1:8000/messages/', json=data)
        self.assertIn("error", response.text)

if __name__ == '__main__':
        unittest.main()
