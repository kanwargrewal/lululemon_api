from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch


class ProductScraperSimpleTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('product-scraper')

    @patch('scrapper.views.requests.get')
    def test_get_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "contents": [{
                "mainContent": [{
                    "contents": [{
                        "records": [{
                            "attributes": {"product.displayName": ["lululemon Align™ High-Rise Ribbed Pant 25\""]}
                        }]
                    }]
                }]
            }]
        }

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("lululemon Align™ High-Rise Ribbed Pant 25\"", response.json()['results'][0]['product_details'])

    def test_post_no_urls_provided(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()['error'], 'No URLs provided')

    @patch('scrapper.views.requests.get')
    def test_post_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "contents": [{
                "mainContent": [{
                    "contents": [{
                        "records": [{
                            "attributes": {"product.displayName": ["lululemon Align™ High-Rise Ribbed Pant 25\""]}
                        }]
                    }]
                }]
            }]
        }

        response = self.client.post(self.url, {"urls": ["https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json"]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("lululemon Align™ High-Rise Ribbed Pant 25\"", response.json()['results'][0]['product_details'])
