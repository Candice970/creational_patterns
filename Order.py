class Order:
    def __init__(self, order_id: str, date: str, status: str):
        self._order_id = order_id
        self._date = date
        self._status = status
        self._products: List[Product] = []

    def place_order(self, products: List[Product]):
        self._products.extend(products)
        self._status = "Placed"

    def cancel_order(self):
        self._status = "Cancelled"
        self._products.clear()

    @property
    def total_amount(self):
        return sum(product.price for product in self._products)
