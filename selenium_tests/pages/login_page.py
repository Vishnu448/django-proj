from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "id_username")  # Update based on your actual HTML
    PASSWORD_FIELD = (By.ID, "id_password")  # Update based on your actual HTML
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")  # Update based on your actual HTML
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")  # Update based on your actual HTML
    
    def open(self):
        self.driver.get(f"{self.base_url}/login/")
        return self
    
    def login(self, username, password):
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        if self.is_element_displayed(self.ERROR_MESSAGE):
            return self.get_element_text(self.ERROR_MESSAGE)
        return None
    
    def is_logged_in(self):
        # Check if redirected to dashboard or some indicator that login was successful
        # This will depend on your application behavior
        return "/dashboard/" in self.driver.current_url or self.is_element_displayed((By.ID, "user-menu"))