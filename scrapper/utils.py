def get_product_details(data):

    results = []
    for content in data.get('contents', []):
        for main_content in content.get('mainContent', []):
            for content in main_content.get('contents', []):
                for record in content.get('records', []):
                    attributes = record.get('attributes', {})
                    product_name = attributes.get('product.displayName')
                    if product_name:
                        results.append(product_name[0])

    return results