class Store:
    def __init__(self):
        self.products = {}
        self.last_product_id = 0

    def add_product(self, product):
        self.last_product_id += 1
        self.products[self.last_product_id] = product
        product._id = self.last_product_id

    def delete_product(self, product_id):
        del self.products[product_id]

    def get_product(self, product_id):
        return self.products[product_id]

    def get_products(self):
        return self.products