from django.conf.urls import url
from django.http import response
from django.test import TestCase
from django.urls import reverse
# response status code 
# template that a view is using 



class SnacksTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_list_page_tepmlate(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')
        self.assertTemplateUsed(response,'_base.html')