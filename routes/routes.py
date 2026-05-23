class Routes:
    Base_url="http://localhost:3000"
    Base_url_cart = "http://localhost:3001"
    #Product Module routes
    Get_All_Products="/products"
    Get_Prod_By_Id="/products/{id}"
    Create_Product="/products"
    Update_Product="/products/{id}"
    Delete_Product="/products/{id}"
    Get_Prod_By_Limit="/products?_limit={limit}"
    Get_Prod_By_Category="/products?_category={category}"

    #Cart Module routes
    Get_All_Cart="/carts"
    Get_cart_by_Id="/carts/{id}"
    Create_Cart = "/carts"
    Update_Cart = "/carts/{id}"
    Delete_Cart = "/carts/{id}"


    
