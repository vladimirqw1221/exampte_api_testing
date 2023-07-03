import allure


class TestRequest:

    @allure.title("Create token")
    @allure.tag("Api")
    @allure.description("Test case for example test with api requests")
    @allure.feature("POST")
    def test_create_token(self, _response):
        _response.create_token_auth()

    @allure.title("Get books")
    @allure.tag("Api")
    @allure.description("Test case for example test with api requests")
    @allure.feature("GET")
    def test_gitting_books(self, _response):
        _response.gitting_books()

    @allure.title("Get books id ")
    @allure.tag("Api")
    @allure.description("Test case for example test with api requests")
    @allure.feature("GET")
    def test_gitting_books_id(self, _response):
        _response.gitting_books_id()

    @allure.title("Create books")
    @allure.tag("Api")
    @allure.description("Test case for example test with api requests")
    @allure.feature("POST")
    def test_create_books(self, _response):
        _response.create_books()

    @allure.title("Update books")
    @allure.tag("Api")
    @allure.description("Test case for example test with api requests")
    @allure.feature("UPDATE")
    def test_update_books_info(self, _response):
        _response.update_books_info()

    @allure.title("Update first name on author")
    @allure.tag("Api")
    @allure.description("Test case for example test with api requests")
    @allure.feature("PATCH")
    def test_updata_first_name(self, _response):
        _response.updata_first_name()

    @allure.title("Delete book")
    @allure.tag("Api")
    @allure.description("Test case for example test with api requests")
    @allure.feature("Delete")
    def test_delete_first_name(self, _response):
        _response.delete_first_name()

    @allure.title("Get status")
    @allure.tag("Api")
    @allure.description("Test case for example test with api requests")
    @allure.feature("POST")
    def test_ping_shop(self, _response):
        _response.ping_shop()
