from datetime import datetime
from typing import List

class Product:
    def __init__(self, product_id: str, name: str, price: float):
        self._product_id = product_id
        self._name = name
        self._price = price

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
