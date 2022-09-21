from django.test import TestCase
from django.test import Client
from django.urls import resolve
from mywatchlist.views import show_mywatchlist, show_xml, show_json

class UnitTest(TestCase):

    def test_mywatchlist_exist(self):
        response = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)

    def test_using_show_mywatchlist(self):
        found = resolve('/mywatchlist/')
        self.assertEqual(found.func, show_mywatchlist)

    def test_data_xml_exist(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_using_show_xml(self):
        found = resolve('/mywatchlist/xml/')
        self.assertEqual(found.func, show_xml)

    def test_data_json_exist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def test_using_show_json(self):
        found = resolve('/mywatchlist/json/')
        self.assertEqual(found.func, show_json)



