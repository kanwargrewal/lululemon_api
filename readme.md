# Product Scraper API

## Overview
This Django project provides a RESTful API endpoint that scrapes product details from test endpoints. It handles requests to fetch product names from URLs either predefined or provided by the user via a POST request, caches these responses for efficiency, and returns the data in a structured JSON format.

## Setup Instructions

### Requirements
- Django
- Django REST Framework
- Requests

### Installation
Install the required packages using pip:
```bash
pip install django djangorestframework requests django-redis
```
## API Reference
### Endpoints
#### 1. Get Product Details from Predefined URLs
```http
GET /api/products/
```
##### Description:
Returns product details from predefined URLs. This endpoint does not require any parameters and is used to quickly access product information from the given URLs.
 - https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json
 - https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json
##### Auth required
No
##### Query Parameters: 
None
##### Response:
```json
{
    "results": [
        {
            "url": "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
            "product_details": [
                "Wunder Train High-Rise Tight 25\"",
                "lululemon Align™ High-Rise Pant 28\"",
                "Wunder Train High-Rise Tight 28\"",
                "lululemon Align™ High-Rise Pant 25\"",
                "lululemon Align™ High-Rise Mini-Flare Pant *Regular",
                "lululemon Align™ High-Rise Pant with Pockets 25\"",
                "lululemon Align™ High-Rise Ribbed Pant 28\"",
                "lululemon Align™ High-Rise Ribbed Pant 25\"",
                "Groove Super-High-Rise Nulu Flared Pant *Regular",
                "lululemon Align™ High-Rise Mini-Flared Pant *Extra Short",
                "lululemon Align™ Super-High-Rise Pant 28\"",
                "Wunder Under SmoothCover High-Rise Tight 25\"",
                "lululemon Align™ High-Rise Crop with Pockets 23\"",
                "Wunder Train High-Rise Tight with Pockets 25\"",
                "lululemon Align™ High-Rise Ribbed Mini-Flare Pant *Regular",
                "lululemon Align™ High-Rise Pant 31\"",
                "Wunder Train High-Rise Crop with Pockets 23\"",
                "lululemon Align™ Mini-Flare Pant *Tall",
                "Wunder Train Contour Fit High-Rise Crop 23\"",
                "lululemon Align™ Low-Rise Pant 25\"",
                "Wunder Train Contour Fit High-Rise Tight with Pockets 25\"",
                "lululemon Align™ High-Rise Pant 25\" *Pride",
                "Wunder Train High-Rise Tight 31\"",
                "lululemon Align™ High-Rise Crop 23\"",
                "lululemon Align™ High-Rise Crop 21\"",
                "lululemon Align™ High-Rise Crop 17\"",
                "lululemon Align™ High-Rise Pant 28\" *Shine",
                "lululemon Align™ Ribbed Mini-Flare Pant *Extra Short",
                "lululemon Align™ High-Rise Pant with Pockets 28\"",
                "Wunder Train High-Rise Crop 23\"",
                "Wunder Train Contour Fit High-Rise Tight 25\"",
                "Wunder Train High-Rise Ribbed Tight 25\"",
                "Wunder Train High-Rise Ribbed Tight 28\"",
                "lululemon Align™ High-Rise Pant 25\" *Shine",
                "lululemon Align™ Asymmetrical-Waist Mini-Flared Pant 32\"",
                "SenseKnit Running High-Rise Tight 28\"",
                "Wunder Train Contour Fit High-Rise Tight 28\"",
                "lululemon Align™ Asymmetrical-Waist Pant 25\"",
                "lululemon Align™ High-Rise Ribbed Crop 23\"",
                "lululemon Align™ Low-Rise Flared Pant 32.5\"",
                "Wunder Train High-Rise Crop 21\"",
                "Fast and Free High-Rise Tight 25” Pockets *Updated",
                "Throwback Print lululemon Align™ High-Rise Pant 25\"",
                "Wunder Train High-Rise Tight with Pockets 28\"",
                "Fast and Free High-Rise Crop 23\" Pockets *Updated",
                "Wunder Under SmoothCover High-Rise Tight 28\"",
                "Wunder Train High-Rise Ribbed Crop 23\"",
                "Wunder Under SmoothCover Tight with Pockets 25\"",
                "Fast and Free High-Rise Tight 28” Pockets *Updated",
                "Groove High-Rise Flared Pant with Pockets 32.5\"",
                "Wunder Train Low-Rise Tight 25\"",
                "Fast and Free High-Rise Crop with Pockets 19\"",
                "lululemon Align™ V-Waist Pant 25\"",
                "lululemon Align™ High-Rise Crop 23\" *Shine",
                "Fast and Free High-Rise Thermal Tight 28\" *Pockets",
                "Fast and Free High-Rise Thermal Tight 25\" *Pockets",
                "lululemon Align™ High-Rise Pant with Pockets 31\"",
                "lululemon Align™ High-Rise Pant 28\"",
                "Fast and Free High-Rise Tight 25\"",
                "lululemon Align™ High-Rise Pant 25\"",
                "lululemon Align™ V-Waist Mini-Flare Pant",
                "Swift Speed High-Rise Tight 28\"",
                "Invigorate High-Rise Tight 25\"",
                "Groove Super-High-Rise Flared Pant Nulu *Regular",
                "Wunder Train High-Rise Tight 28\" *Foil",
                "Swift Speed High-Rise Crop 21\"",
                "Base Pace High-Rise Tight 25\"",
                "Wunder Train High-Rise Tight 25\" *Foil",
                "Swift Speed High-Rise Tight 28\" *Brushed Luxtreme",
                "All the Right Places High-Rise Drawcord Waist Crop 23”",
                "lululemon Align™ High-Rise Pant with Pockets 25\"",
                "lululemon Align™ High-Rise Ribbed Pant 28\" *Shine",
                "Wunder Train Mesh High-Rise Tight 25\"",
                "Fast and Free High-Rise Tight 25” Pockets *Updated",
                "lululemon Align™ High-Rise Mini-Flare Pant *Regular",
                "lululemon Align™ High-Rise Wide-Leg Pant *Regular",
                "Wunder Train High-Rise Crop 23\"",
                "Wunder Train High-Rise Ribbed Tight 28\"",
                "Wunder Train High-Rise Tight 25\"",
                "lululemon Align™ High-Rise Ribbed Wide-Leg Pant *Tall",
                "Nulux Reflective High-Rise Track Tight 25\"",
                "Wunder Train High-Rise Ribbed Tight 25\"",
                "Base Pace High-Rise Crop 23\"",
                "lululemon Align™ High-Rise Ribbed Mini-Flare Pant *Regular",
                "lululemon Align™ High-Rise Mini-Flare Pant *Extra Short",
                "lululemon Align™ High-Rise Mini-Flare Pant *Extra Short",
                "V-Waist Yoga Tight 25\" *Grid Texture",
                "Fast and Free High-Rise Tight 28” Pockets *Updated",
                "Wunder Train High-Rise Tight 28\"",
                "Wunder Train Contour Fit High-Rise Tight 28\"",
                "Wunder Train Contour Fit High-Rise Tight 25\"",
                "Wunder Train High-Rise Tight with Pockets 25\"",
                "lululemon Align™ High-Rise Crop 21\"",
                "Wunder Train High-Rise Crop 23\" *Foil",
                "lululemon Align™ High-Rise Ribbed Pant 28\"",
                "lululemon Align™ High-Rise Ribbed Pant 25\"",
                "lululemon Align™ High-Rise Pant with Pockets 28\"",
                "Fast and Free High-Rise Crop 23\"",
                "lululemon Align™ Ribbed Mini-Flare Pant *Extra Short",
                "Wunder Under High-Rise Tight 25\" *Shine",
                "lululemon Align™ High-Rise Crop 23\"",
                "lululemon Align™ Low-Rise Pant 25\"",
                "lululemon Align™ Asymmetrical-Waist Mini-Flare Pant 32\"",
                "High-Rise Base Layer Tight 28\"",
                "Fast and Free High-Rise Tight 25\" *Colour Block",
                "lululemon Align™ V-Waist Pant 25\"",
                "lululemon Align™ Ribbed Mini-Flare Pant *Extra Short",
                "Wunder Train Aerobic High-Rise Tight 25\" *Twill",
                "Fast and Free High-Rise Crop 19\"",
                "InStill High-Rise Tight 25\"",
                "SenseKnit Running High-Rise Tight 28\"",
                "Cold Weather High-Rise Running Tight 28\"",
                "Groove Super-High-Rise Crop 23\" *Nulu",
                "SenseKnit High-Rise Running Tight 28\"",
                "Everlux and Mesh Super-High-Rise Training Tight 25\""
            ]
        },
        {
            "url": "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json",
            "product_details": [
                "Classic Unisex Ball Cap *Wordmark",
                "Fast and Free Running Hat",
                "Classic Unisex Ball Cap",
                "Fast and Free Running Hat *WovenAir",
                "Men's Fast and Free Running Hat",
                "Men's Days Shade Ball Cap *Logo",
                "Men's Fast and Free Running Hat",
                "Multi-Panel Hat",
                "High Ventilation Running Hat"
            ]
        }
    ]
}
```
#### 2. Get Product Details from dynamic URLs
```http
POST /api/products/
```
##### Description: 
Allows you to submit a list of URLs from which to fetch product details. This endpoint is flexible and can handle dynamic URL requests.
##### Auth required
No
##### Request Body:
```json
{
  "urls": ["https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json"]
}

```
##### Response:
```json
{
    "results": [
        {
            "url": "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
            "product_details": [
                "Wunder Train High-Rise Tight 25\"",
                "lululemon Align™ High-Rise Pant 28\"",
                "Wunder Train High-Rise Tight 28\"",
                "lululemon Align™ High-Rise Pant 25\"",
                "lululemon Align™ High-Rise Mini-Flare Pant *Regular",
                "lululemon Align™ High-Rise Pant with Pockets 25\"",
                "lululemon Align™ High-Rise Ribbed Pant 28\"",
                "lululemon Align™ High-Rise Ribbed Pant 25\"",
                "Groove Super-High-Rise Nulu Flared Pant *Regular",
                "lululemon Align™ High-Rise Mini-Flared Pant *Extra Short",
                "lululemon Align™ Super-High-Rise Pant 28\"",
                "Wunder Under SmoothCover High-Rise Tight 25\"",
                "lululemon Align™ High-Rise Crop with Pockets 23\"",
                "Wunder Train High-Rise Tight with Pockets 25\"",
                "lululemon Align™ High-Rise Ribbed Mini-Flare Pant *Regular",
                "lululemon Align™ High-Rise Pant 31\"",
                "Wunder Train High-Rise Crop with Pockets 23\"",
                "lululemon Align™ Mini-Flare Pant *Tall",
                "Wunder Train Contour Fit High-Rise Crop 23\"",
                "lululemon Align™ Low-Rise Pant 25\"",
                "Wunder Train Contour Fit High-Rise Tight with Pockets 25\"",
                "lululemon Align™ High-Rise Pant 25\" *Pride",
                "Wunder Train High-Rise Tight 31\"",
                "lululemon Align™ High-Rise Crop 23\"",
                "lululemon Align™ High-Rise Crop 21\"",
                "lululemon Align™ High-Rise Crop 17\"",
                "lululemon Align™ High-Rise Pant 28\" *Shine",
                "lululemon Align™ Ribbed Mini-Flare Pant *Extra Short",
                "lululemon Align™ High-Rise Pant with Pockets 28\"",
                "Wunder Train High-Rise Crop 23\"",
                "Wunder Train Contour Fit High-Rise Tight 25\"",
                "Wunder Train High-Rise Ribbed Tight 25\"",
                "Wunder Train High-Rise Ribbed Tight 28\"",
                "lululemon Align™ High-Rise Pant 25\" *Shine",
                "lululemon Align™ Asymmetrical-Waist Mini-Flared Pant 32\"",
                "SenseKnit Running High-Rise Tight 28\"",
                "Wunder Train Contour Fit High-Rise Tight 28\"",
                "lululemon Align™ Asymmetrical-Waist Pant 25\"",
                "lululemon Align™ High-Rise Ribbed Crop 23\"",
                "lululemon Align™ Low-Rise Flared Pant 32.5\"",
                "Wunder Train High-Rise Crop 21\"",
                "Fast and Free High-Rise Tight 25” Pockets *Updated",
                "Throwback Print lululemon Align™ High-Rise Pant 25\"",
                "Wunder Train High-Rise Tight with Pockets 28\"",
                "Fast and Free High-Rise Crop 23\" Pockets *Updated",
                "Wunder Under SmoothCover High-Rise Tight 28\"",
                "Wunder Train High-Rise Ribbed Crop 23\"",
                "Wunder Under SmoothCover Tight with Pockets 25\"",
                "Fast and Free High-Rise Tight 28” Pockets *Updated",
                "Groove High-Rise Flared Pant with Pockets 32.5\"",
                "Wunder Train Low-Rise Tight 25\"",
                "Fast and Free High-Rise Crop with Pockets 19\"",
                "lululemon Align™ V-Waist Pant 25\"",
                "lululemon Align™ High-Rise Crop 23\" *Shine",
                "Fast and Free High-Rise Thermal Tight 28\" *Pockets",
                "Fast and Free High-Rise Thermal Tight 25\" *Pockets",
                "lululemon Align™ High-Rise Pant with Pockets 31\"",
                "lululemon Align™ High-Rise Pant 28\"",
                "Fast and Free High-Rise Tight 25\"",
                "lululemon Align™ High-Rise Pant 25\"",
                "lululemon Align™ V-Waist Mini-Flare Pant",
                "Swift Speed High-Rise Tight 28\"",
                "Invigorate High-Rise Tight 25\"",
                "Groove Super-High-Rise Flared Pant Nulu *Regular",
                "Wunder Train High-Rise Tight 28\" *Foil",
                "Swift Speed High-Rise Crop 21\"",
                "Base Pace High-Rise Tight 25\"",
                "Wunder Train High-Rise Tight 25\" *Foil",
                "Swift Speed High-Rise Tight 28\" *Brushed Luxtreme",
                "All the Right Places High-Rise Drawcord Waist Crop 23”",
                "lululemon Align™ High-Rise Pant with Pockets 25\"",
                "lululemon Align™ High-Rise Ribbed Pant 28\" *Shine",
                "Wunder Train Mesh High-Rise Tight 25\"",
                "Fast and Free High-Rise Tight 25” Pockets *Updated",
                "lululemon Align™ High-Rise Mini-Flare Pant *Regular",
                "lululemon Align™ High-Rise Wide-Leg Pant *Regular",
                "Wunder Train High-Rise Crop 23\"",
                "Wunder Train High-Rise Ribbed Tight 28\"",
                "Wunder Train High-Rise Tight 25\"",
                "lululemon Align™ High-Rise Ribbed Wide-Leg Pant *Tall",
                "Nulux Reflective High-Rise Track Tight 25\"",
                "Wunder Train High-Rise Ribbed Tight 25\"",
                "Base Pace High-Rise Crop 23\"",
                "lululemon Align™ High-Rise Ribbed Mini-Flare Pant *Regular",
                "lululemon Align™ High-Rise Mini-Flare Pant *Extra Short",
                "lululemon Align™ High-Rise Mini-Flare Pant *Extra Short",
                "V-Waist Yoga Tight 25\" *Grid Texture",
                "Fast and Free High-Rise Tight 28” Pockets *Updated",
                "Wunder Train High-Rise Tight 28\"",
                "Wunder Train Contour Fit High-Rise Tight 28\"",
                "Wunder Train Contour Fit High-Rise Tight 25\"",
                "Wunder Train High-Rise Tight with Pockets 25\"",
                "lululemon Align™ High-Rise Crop 21\"",
                "Wunder Train High-Rise Crop 23\" *Foil",
                "lululemon Align™ High-Rise Ribbed Pant 28\"",
                "lululemon Align™ High-Rise Ribbed Pant 25\"",
                "lululemon Align™ High-Rise Pant with Pockets 28\"",
                "Fast and Free High-Rise Crop 23\"",
                "lululemon Align™ Ribbed Mini-Flare Pant *Extra Short",
                "Wunder Under High-Rise Tight 25\" *Shine",
                "lululemon Align™ High-Rise Crop 23\"",
                "lululemon Align™ Low-Rise Pant 25\"",
                "lululemon Align™ Asymmetrical-Waist Mini-Flare Pant 32\"",
                "High-Rise Base Layer Tight 28\"",
                "Fast and Free High-Rise Tight 25\" *Colour Block",
                "lululemon Align™ V-Waist Pant 25\"",
                "lululemon Align™ Ribbed Mini-Flare Pant *Extra Short",
                "Wunder Train Aerobic High-Rise Tight 25\" *Twill",
                "Fast and Free High-Rise Crop 19\"",
                "InStill High-Rise Tight 25\"",
                "SenseKnit Running High-Rise Tight 28\"",
                "Cold Weather High-Rise Running Tight 28\"",
                "Groove Super-High-Rise Crop 23\" *Nulu",
                "SenseKnit High-Rise Running Tight 28\"",
                "Everlux and Mesh Super-High-Rise Training Tight 25\""
            ]
        },
        {
            "url": "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json",
            "product_details": [
                "Classic Unisex Ball Cap *Wordmark",
                "Fast and Free Running Hat",
                "Classic Unisex Ball Cap",
                "Fast and Free Running Hat *WovenAir",
                "Men's Fast and Free Running Hat",
                "Men's Days Shade Ball Cap *Logo",
                "Men's Fast and Free Running Hat",
                "Multi-Panel Hat",
                "High Ventilation Running Hat"
            ]
        }
    ]
}
```
