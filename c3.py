def linear_search_product(products, target):
    indices = []
    for i, product in enumerate(products):
        if product == target:
            indices.append(i)
    return indices
