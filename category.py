
class Category:
    def __init__(self, category_id: str, name: str):
        self._category_id = category_id
        self._name = name
        self._products: List[Product] = []

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product: Product):
        self._products.remove(product)
