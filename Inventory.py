class InventoryLog:
    def __init__(self, log_id: str, action: str, product_id: str):
        self._log_id = log_id
        self._timestamp = datetime.now()
        self._action = action
        self._product_id = product_id

    def record_action(self):
        print(f"[{self._timestamp}] Action: {self._action} on Product ID: {self._product_id}")
