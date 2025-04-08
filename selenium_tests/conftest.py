import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.video_recorder import VideoRecorder

@pytest.fixture(scope="function")
def driver(request):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless for server environment
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Create the driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Set up video recording
    video_dir = os.path.join(os.getcwd(), "test_videos")
    os.makedirs(video_dir, exist_ok=True)
    test_name = request.node.name
    recorder = VideoRecorder(driver, os.path.join(video_dir, f"{test_name}.mp4"))
    recorder.start()
    
    # Provide the driver to the test
    yield driver
    
    # Clean up
    recorder.stop()
    driver.quit()

@pytest.fixture
def base_url():
    # Return the URL of your Django app
    return "http://localhost:8000"  # Adjust based on your setup