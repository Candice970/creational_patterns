class User:
    def __init__(self, user_id: str, name: str, role: str):
        self._user_id = user_id
        self._name = name
        self._role = role
        self._orders: List[Order] = []

    def login(self) -> bool:
        return True  # Simulate login logic

    def place_order(self, order: Order):
        self._orders.append(order)
