from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains, Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class labourMedia:
    # locators
    media_locator = "//a[text() = 'Media']"
    photo_gall_locator = "//a[text() = 'Photo Gallery']"
    img_src_locator = "//a[text()='10th International Yoga Day, 2024']"
    image1 = "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/ul/li[1]/div[1]/div/a/img"
    image2 = "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/ul/li[2]/div[1]/div/a/img"

    # constructor intializing url and driver
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Method to launch url and maximize window
    def homePageLaunch(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            return True
        except:
            print("Error")
            return False

    # Method to hover media link
    def mediaPageLaunch(self):
        try:
            media_element = self.driver.find_element(by=By.XPATH, value=self.media_locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(media_element).perform()
            sleep(2)
            return True
        except:
            print("Error clicking the element")
            return False

    # Method to click on photo gallery link
    def photoGalLaunch(self):
        try:
            self.driver.find_element(by=By.XPATH, value=self.photo_gall_locator).click()
            sleep(2)
            return True
        except:
            print("Error accessing link")
            return False

    # Method to download images
    def image_download(self):
        imglink = self.driver.find_element(by=By.XPATH, value=self.img_src_locator)
        imglink.click()
        sleep(5)
        # code to scroll, so that image element can be found
        self.driver.execute_script("window.scrollBy(0,100)", "")
        image1link = self.driver.find_element(by=By.XPATH, value=self.image1)
        image1link.screenshot("D:\\VinoLEarning\\PySelProject\\Images\\image1.png")
        # code to scroll further, so that second image can be found
        self.driver.execute_script("window.scrollBy(100,500)", "")
        image2link = self.driver.find_element(by=By.XPATH, value=self.image2)
        image2link.screenshot("D:\\VinoLEarning\\PySelProject\\Images\\image2.png")
        return True

    def shutdown(self):
        try:
            self.driver.quit()
            return True
        except:
            print("Error closing the web page")
            return False


if __name__ == "__main__":
    lm = labourMedia("https://labour.gov.in")
    lm.homePageLaunch()
    lm.mediaPageLaunch()
    lm.photoGalLaunch()
    lm.image_download()
    lm.shutdown()
