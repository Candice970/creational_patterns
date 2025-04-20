class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_info: str):
        self._supplier_id = supplier_id
        self._name = name
        self._contact_info = contact_info
        self._products: List[Product] = []

    def supply_product(self, product: Product):
        self._products.append(product)
