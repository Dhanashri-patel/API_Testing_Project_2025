import os
import pytest
import requests
from utils.dataProvider import read_with_json, read_with_excel, read_with_csv
from datamodels.products import Product
from routes.routes import Routes

path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../testdata/productdata.json"))
excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../testdata/products_data.xlsx"))
csv_path= os.path.abspath(os.path.join(os.path.dirname(__file__),"../testdata/products_data.csv"))

class TestDataDrivenProducts_API:

    @pytest.fixture(autouse=True)
    def init_class_var(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]

    @pytest.mark.parametrize("product_test_data",read_with_json(path))
    def test_create_delete_product_json(self, product_test_data):
        product_data=product_test_data[0]
        title = product_data["title"]
        description = product_data["description"]
        price = product_data["price"]
        category = product_data["category"]
        stock = product_data["stock"]

        payload = Product(title,price,description,category,stock)

        #create product request
        response = requests.post(self.base_url+Routes.Create_Product, json=payload.__dict__)
        data = response.json()
        product_id = data["id"]
        assert response.status_code == 201 , "Wrong Status Code, Product creation failed..."
        assert data["title"] == title , "Wrong title used"

        # delete product
        response = requests.delete(self.base_url + Routes.Delete_Product.format(id=product_id))
        assert response.status_code == 200, "Wrong Status Code, Product deletion failed..."


    @pytest.mark.parametrize("product_test_data", read_with_excel(excel_path,"products_data"))
    def test_create_delete_product_excel(self,product_test_data):
        product_data = product_test_data
        title = product_data["title"]
        description = product_data["description"]
        price = product_data["price"]
        category = product_data["category"]
        stock = product_data["stock"]

        payload = Product(title, price, description, category, stock)

        # create product request
        response = requests.post(self.base_url + Routes.Create_Product, json=payload.__dict__)
        data = response.json()
        product_id = data["id"]
        assert response.status_code == 201, "Wrong Status Code, Product creation failed..."
        assert data["title"] == title, "Wrong title used"

        # delete product
        response = requests.delete(self.base_url + Routes.Delete_Product.format(id=product_id))
        assert response.status_code == 200, "Wrong Status Code, Product deletion failed..."

    @pytest.mark.parametrize("product_test_data", read_with_csv(csv_path))
    def test_create_delete_product_csv(self,product_test_data):
        product_data = product_test_data
        title = product_data["title"]
        description = product_data["description"]
        price = product_data["price"]
        category = product_data["category"]
        stock = product_data["stock"]

        payload = Product(title, price, description, category, stock)

        # create product request
        response = requests.post(self.base_url + Routes.Create_Product, json=payload.__dict__)
        data = response.json()
        product_id = data["id"]
        assert response.status_code == 201, "Wrong Status Code, Product creation failed..."
        assert data["title"] == title, "Wrong title used"

        # delete product
        response = requests.delete(self.base_url + Routes.Delete_Product.format(id=product_id))
        assert response.status_code == 200, "Wrong Status Code, Product deletion failed..."



