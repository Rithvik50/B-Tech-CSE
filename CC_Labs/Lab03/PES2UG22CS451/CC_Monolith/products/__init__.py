from Lab3.PES2UG22CS451.CC_Monolith.products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


# def list_products() -> list[Product]:
#     products = dao.list_products()
#     result = []
#     for product in products:
#         result.append(Product.load(product))
    
#     return result

def list_products() -> list[Product]: #Optimization
    return list(map(Product.load, dao.list_products()))



def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)


