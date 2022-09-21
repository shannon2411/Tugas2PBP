from django.test import TestCase
from django.urls import reverse
from mywatchlist.views import show_json, show_xml, show_watchlist

class TestUrls(TestCase):
    def test_html_url(self):
        response = self.client.get(reverse("mywatchlist:show_watchlist"))
        self.assertEquals(response.status_code, 200)

    def test_json_url(self):
        response= self.client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        response = self.client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code, 200)