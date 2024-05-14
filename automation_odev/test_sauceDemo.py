import pytest


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support import expected_conditions as EC



class Test_sauceDemo:
    def setup_method(self): 
        # peş peşe testlerde, her test öncesi çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):  
        # her test bitiminde çalışacak fonksiyon.
        self.driver.quit()   
        
#1)Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys() 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce") 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username is required"

#2) Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

    def test_two_invalid_login(self): 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user") 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Password is required"

 #3)Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
       
    def test_locked_login(self): 
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

#4)Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")
        testResult = len(products)
        if testResult == 6: 
            print("TEST SONUCU:  True")
        else:
            print("TEST SONUCU:  False")  

#5)Add to cart butonuna tıkladığında sepete gidip eklenip eklenmediğini kontrol etmek
    
    def test_valid_login(self):
        self.login("standard_user", "secret_sauce")
        assert "inventory.html" in self.driver.current_url

    def test_add_to_cart(self):
        self.login("standard_user", "secret_sauce")
        self.add_to_cart()
        assert self.is_cart_contains_item(), "Ürün sepete eklenemedi."

    def test_add_to_cart(self):
        self.login("standard_user", "secret_sauce")
        self.add_to_cart()
        assert self.is_cart_contains_item(), "Ürün sepete eklenemedi."
    
    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)
        
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys(password)
        
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        
    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        add_to_cart_button.click()

    def is_cart_contains_item(self):
        shopping_cart_container = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        shopping_cart_container.click()
        cart_items = self.driver.find_elements(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]')
        return len(cart_items) > 0

#6) Başarılı giriş yaptıktan sonra sepete ekleyip satın alma işlemini tamamlar.
    
    def test_valid_login(self):
        username = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username.send_keys("standard_user")
        password = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "password")))
        password.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
    
    #test_add_to_cart(self):
        
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        add_to_cart_button.click()
        go_to_basket = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        go_to_basket.click()
        checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
        checkout_button.click()

    #test_checkout_information(self):
        first_name = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name.send_keys("Özge")
        last_name = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "last-name")))
        last_name.send_keys("ÇAM")
        postal_code = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "postal-code")))
        postal_code.send_keys("34515")
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))
        continue_button.click()

    #test_finish_shopping(self):
        finish_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]')))
        finish_button.click()
        thank_you_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_complete_container"]/h2')))
        assert thank_you_message.text == "Thank you for your order!"


#7)Parametrize fonksiyonu ile 3 farklı veriyle test

    @pytest.mark.parametrize("credentials", [
            {"username": "standard_user", "password": "secret_sauce", "expected_success": True, "error_message": ""},
            {"username": "locked_out_user", "password": "secret_sauce", "expected_success": False, "error_message": "Epic sadface: Sorry, this user has been locked out."},
            {"username": "deneme_test", "password": "secret_sauce", "expected_success": False, "error_message": "Epic sadface: Username and password do not match any user in this service"},
        ])
    def test_login(self, credentials):
            usernameInput = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "user-name")))
            usernameInput.send_keys(credentials["username"])
            passwordInput = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "password")))
            passwordInput.send_keys(credentials["password"])
            loginButton = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "login-button")))
            loginButton.click()

            # Başarılı veya başarısız giriş durumunu kontrol et
            if credentials["expected_success"]:
                assert "inventory.html" in self.driver.current_url
                print(f"{credentials['username']} kullanıcısı başarıyla giriş yaptı.")
            else:
                # Hata mesajını kontrol et ve doğru mesajı yazdır
                error_message_element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')))
                assert error_message_element.text == credentials["error_message"]
                print(f"{credentials['username']} kullanıcısı giriş yapamadı. Hata Mesajı: {credentials['error_message']}")

    if __name__ == "__main__":
        pytest.main(["-v", "--html=report.html"])

#8)Başarılı giriş yapar ardından çıkış yapar.

    def test_exit_login(self):
        username = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user") # kullanıcı başarılı girer
        password = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce") # şifre girer 
        login_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"login-button")))
        login_button.click()

        assert "inventory.html" in self.driver.current_url
        print("successful entry")

                        
        
            

