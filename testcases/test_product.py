import pytest
import requests

from routes.routes import Routes
from payloads.payload import Payload
from datamodels.products import Product

new_product_id=None

class TestProduct:

    @pytest.fixture(autouse=True)
    def init_class_var(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.category= "Fitness"
        self.payload = Payload().product_payload()

    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_get_all_products(self):
        res = requests.get(self.base_url+Routes.Get_All_Products)
        data=res.json()
        assert res.status_code == 200, "Wrong status code"

    @pytest.mark.regression
    @pytest.mark.order(5)
    def test_get_product_by_id(self):
        #product_id = self.config.get_property("productId")

        res= requests.get(self.base_url+Routes.Get_Prod_By_Id.format(id=new_product_id))
        assert res.status_code == 200, "Wrong status code"

    @pytest.mark.sanity
    @pytest.mark.order(2)
    def test_get_product_by_limit(self):
        limit = self.config.get_property("limit")
        res= requests.get(self.base_url+Routes.Get_Prod_By_Limit.format(limit=limit))
        assert res.status_code == 200, "Wrong status code"

    @pytest.mark.sanity
    @pytest.mark.order(3)
    def test_get_product_by_category(self):
        #limit = self.config.get_property("limit")
        res= requests.get(self.base_url+Routes.Get_Prod_By_Category.format(category=self.category))
        assert res.status_code == 200, "Wrong status code"

    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_create_product(self):
        global new_product_id
        res= requests.post(self.base_url+Routes.Create_Product, json=self.payload.__dict__)
        data=res.json()
        assert res.status_code == 201, "Wrong status code"
        assert data["title"] == self.payload.__dict__["title"]
        new_product_id=data["id"]

    @pytest.mark.regression
    @pytest.mark.order(6)
    def test_update_product(self):
        res= requests.put(self.base_url+Routes.Update_Product.format(id=new_product_id), json=self.payload.__dict__)
        data=res.json()
        assert res.status_code == 200, "Wrong status code"

    @pytest.mark.regression
    @pytest.mark.order(7)
    def test_delete_product(self):
        res= requests.delete(self.base_url+Routes.Delete_Product.format(id=new_product_id))
        assert res.status_code == 200, "Wrong status code"
