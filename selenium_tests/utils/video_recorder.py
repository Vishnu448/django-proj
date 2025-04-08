import threading
import time
import cv2
import numpy as np
from PIL import ImageGrab
from selenium.webdriver.support.ui import WebDriverWait

class VideoRecorder:
    def __init__(self, driver, output_path, fps=10):
        self.driver = driver
        self.output_path = output_path
        self.fps = fps
        self.is_recording = False
        self.thread = None
    
    def start(self):
        self.is_recording = True
        self.thread = threading.Thread(target=self._record)
        self.thread.start()
    
    def stop(self):
        self.is_recording = False
        if self.thread is not None:
            self.thread.join()
    
    def _record(self):
        # Get the window size
        width = self.driver.execute_script("return window.outerWidth")
        height = self.driver.execute_script("return window.outerHeight")
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_path, fourcc, self.fps, (width, height))
        
        # Start recording
        while self.is_recording:
            # Capture screenshot
            screenshot = ImageGrab.grab(bbox=(0, 0, width, height))
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Write to video
            out.write(frame)
            
            # Control frame rate
            time.sleep(1/self.fps)
        
        # Release resources
        out.release()