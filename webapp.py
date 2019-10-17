from selenium import webdriver
class WebApp:
    instance = None
    driver=None 
    driverpath="c:/webdrivers/Chrome77/chromedriver.exe"
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance
    def __init__(self):
        self.driver=webdriver.Chrome(self.driverpath)
    
    def get_driver(self):
        return self.driver
         
    def setUp(self):
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
    
    def tearDown(self):
        #self.driver.implicitly_wait(5)
        if self.driver is not None:
            self.driver.quit()  

webapp = WebApp.get_instance()
 
