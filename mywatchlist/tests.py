from unittest import result
from django.test import TestCase, Client

# Create your tests here.
class MyWatchListTesting(TestCase):
    def tes_url_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    def tes_url_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
    def tes_url_json(self):
        response = Client().get('mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
