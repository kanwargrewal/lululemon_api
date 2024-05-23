from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch


class ProductScraperSimpleTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('product-scraper')

    @patch('scrapper.views.requests.get')
    def test_get_success(self, mock_get):
        # Setup mock response for a successful API call
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

        # Perform GET request
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("lululemon Align™ High-Rise Ribbed Pant 25\"", response.json()['results'][0]['product_details'])

    def test_post_no_urls_provided(self):
        # Perform POST request with empty data
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()['error'], 'No URLs provided')

    @patch('scrapper.views.requests.get')
    def test_post_success(self, mock_get):
        # Setup mock response for a successful API call
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

        # Perform POST request with URL data
        response = self.client.post(self.url, {"urls": ["https://dummyurl.com"]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("lululemon Align™ High-Rise Ribbed Pant 25\"", response.json()['results'][0]['product_details'])
