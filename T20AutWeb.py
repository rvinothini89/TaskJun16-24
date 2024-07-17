# Task to launch cowin website, navigating across child windows and priting respective window handle

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class coWin:
    #Locators for each element
    faq_locator = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"
    partner_locator = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # method to launch homepage and child pages
    def PagesLaunch(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            homePage_window_handle = self.driver.current_window_handle
            print("Homepage window handle is:", homePage_window_handle)
            # Navigating to faq link
            self.driver.find_element(by=By.XPATH, value=self.faq_locator).click()
            sleep(2)
            # Navigating to partner link
            self.driver.find_element(by=By.XPATH, value=self.partner_locator).click()
            sleep(2)
            all_window_handles = self.driver.window_handles
            # with these lines printing window handle for all child pages and closing all child pages
            for windows in all_window_handles:
                if windows != homePage_window_handle:
                    self.driver.switch_to.window(windows)
                    print("The child window handle is: ", windows)
                    print(self.driver.current_url)
                    self.driver.close()
            # After closing other links and coming back to homepage9999999999999999
            self.driver.switch_to.window(homePage_window_handle)
            return True
        except:
            return False

    def shutdown(self):
        self.driver.quit()
        return None


if __name__ == "__main__":
    cw = coWin("https://www.cowin.gov.in/")
    cw.PagesLaunch()
    cw.shutdown()
