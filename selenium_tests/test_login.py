import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_successful_login(self, driver, base_url):
        """Test that a user can successfully log in with valid credentials."""
        login_page = LoginPage(driver, base_url)
        login_page.open()
        
        # Use test credentials
        login_page.login("testuser", "password123")
        
        # Verify successful login
        assert login_page.is_logged_in(), "Login was not successful"
    
    def test_invalid_credentials(self, driver, base_url):
        """Test that appropriate error is shown with invalid credentials."""
        login_page = LoginPage(driver, base_url)
        login_page.open()
        
        # Use invalid credentials
        login_page.login("invalid_user", "wrong_password")
        
        # Verify error message
        error_message = login_page.get_error_message()
        assert error_message, "No error message displayed for invalid credentials"
        assert "invalid" in error_message.lower() or "incorrect" in error_message.lower()
    
    def test_empty_credentials(self, driver, base_url):
        """Test that form validation works for empty fields."""
        login_page = LoginPage(driver, base_url)
        login_page.open()
        
        # Submit empty form
        login_page.login("", "")
        
        # Verify user is not logged in
        assert not login_page.is_logged_in(), "Login succeeded with empty credentials"