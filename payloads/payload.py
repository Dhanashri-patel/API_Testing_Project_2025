from _datetime import datetime
from faker import Faker
import random
from unicodedata import category

from datamodels.cart import Cart
from datamodels.cartItem import CartItem
from datamodels.products import Product


class Payload:
    fakers = Faker()
    category = ["electronics", "bags", "furniture", "fitness", "home", "wearable"]

    def product_payload(self):
        title = self.fakers.unique.catch_phrase()
        price = float(self.fakers.pricetag().replace("$","").replace(",",""))
        description = self.fakers.sentence()
        category = random.choice(self.category)
        stock = random.randint(1,100)

        return Product(title, price, description, category, stock)


    def cart_payload(self):
        userId = random.randint(1,100)
        date = datetime.now().strftime("%Y-%m-%d")


        products= []
        no_of_products = random.randint(1,5)

        for i in range(no_of_products):
            product = CartItem(
                productId=random.randint(1,10),
                quantity=random.randint(1,5)
            )

            products.append(product)

        return Cart(userId, date, products)
