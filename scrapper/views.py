from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .utils import get_product_details
import requests


CACHE_TIMEOUT = 300

class ProductScraper(APIView):
    def handle_urls(self, urls):
        if not urls:
            return JsonResponse({'error': 'No URLs provided'}, status=status.HTTP_400_BAD_REQUEST)

        results, error = self.scrape_urls(urls)
        if error:
            return JsonResponse({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'results': results}, status=status.HTTP_200_OK)

    def get(self, request):
        predefined_urls = [
            "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
            "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
        ]
        return self.handle_urls(predefined_urls)

    def post(self, request):
        user_urls = request.data.get('urls', [])
        return self.handle_urls(user_urls)

    def scrape_urls(self, urls):
        results = []
        for url in urls:
            cached_data = cache.get(url)
            if not cached_data:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    product_details = get_product_details(data)
                    cache.set(url, product_details, timeout=CACHE_TIMEOUT)
                    results.append({"url": url, "product_details": product_details})
                else:
                    return [], f'Failed to fetch data from {url}'
            else:
                results.append({"url": url, "product_details": cached_data})
        return results, None
