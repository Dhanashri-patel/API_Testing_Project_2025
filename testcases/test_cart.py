from dataclasses import asdict

import pytest
import requests

from payloads.payload import Payload
from routes.routes import Routes

global new_cart_id
class TestCart:

    @pytest.fixture(autouse=True)
    def init_cls_var(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.payload = Payload().cart_payload()

    @pytest.mark.order(1)
    def test_get_all_cart_item(self):
        res=requests.get(self.base_url+Routes.Get_All_Cart)
        assert res.status_code == 200, "Wrong status code"

    @pytest.mark.order(3)
    def test_get_cart_item_by_id(self):
        res=requests.get(self.base_url+Routes.Get_cart_by_Id.format(id=new_cart_id))
        assert res.status_code == 200, "Wrong status code"

    @pytest.mark.order(2)
    def test_create_cart_item(self):
        global new_cart_id
        res = requests.post(self.base_url+Routes.Create_Cart, json=asdict(self.payload))
        data = res.json()
        new_cart_id = data["id"]
        assert res.status_code == 201, "Wrong status code...cart Item creation failed"
        assert data["userId"] == self.payload.userId , "Wrong user ID"

    @pytest.mark.order(4)
    def test_update_cart_item(self):
        res = requests.put(self.base_url+Routes.Update_Cart.format(id=new_cart_id), json=asdict(self.payload))
        assert res.status_code == 200, "Wrong status code...cart Item updation failed"

    @pytest.mark.order(5)
    def test_delete_cart_item(self):
        res = requests.delete(self.base_url+Routes.Update_Cart.format(id=new_cart_id))
        assert res.status_code == 200, "Wrong status code...cart Item deletion failed"