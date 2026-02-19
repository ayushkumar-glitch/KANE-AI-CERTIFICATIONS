
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : Open https://ecommerce-playground.lambdatest.io/
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.implicitly_wait(6)

    # Step - 2 : Click 'Search for Products' searchbar
    element_locators = ["//div[@id='entry_217822']/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 3 : Type 'iphone16'
    element_locators = ["//div[@id='entry_217822']/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'iphone16':
            element.send_keys(char)
    else:
        element.send_keys('iphone16')
    driver.implicitly_wait(6)

    # Step - 4 : Click SEARCH button
    element_locators = ["//div[@id='entry_217822']/div[1]/form[1]/div[1]/div[2]/button[1]", "//button[text()='Search']", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)', "//button[contains(text(),'Search')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : Click 'Search Criteria' input box
    element_locators = ["//input[@id='input-search' and @name='search']", "//input[@placeholder='Keywords' and @type='text']", '#input-search', '[placeholder="Keywords"][name="search"]', '[placeholder="Keywords"][type="text"]', '#input-search[placeholder="Keywords"]', "//input[@placeholder='Keywords' and @name='search']", "//input[contains(@placeholder,'Keywords')]", "//div[contains(@class,'border')]/div[1]/div[1]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 6 : Clear 'Search Criteria' input box
    element_locators = ["//input[@id='input-search' and @name='search']", "//input[@placeholder='Keywords' and @type='text']", '#input-search', '[placeholder="Keywords"][name="search"]', '[placeholder="Keywords"][type="text"]', '#input-search[placeholder="Keywords"]', "//input[@placeholder='Keywords' and @name='search']", "//input[contains(@placeholder,'Keywords')]", "//div[contains(@class,'border')]/div[1]/div[1]/input[1]"]
    element = get_element(driver,element_locators)

    current_value = element.get_attribute('value')
    if current_value:
        n = len(current_value)
        for i in range(n):
            element.send_keys(Keys.BACKSPACE)
    if element.get_attribute("contenteditable") == "true":
        driver.execute_script("arguments[0].innerText = '';", element)
    driver.implicitly_wait(6)

    # Step - 7 : Type 'iphone' in Search Criteria input box
    element_locators = ["//input[@id='input-search' and @name='search']", "//input[@placeholder='Keywords' and @type='text']", '#input-search', '[placeholder="Keywords"][name="search"]', '[placeholder="Keywords"][type="text"]', '#input-search[placeholder="Keywords"]', "//input[@placeholder='Keywords' and @name='search']", "//input[contains(@placeholder,'Keywords')]", "//div[contains(@class,'border')]/div[1]/div[1]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'iphone':
            element.send_keys(char)
    else:
        element.send_keys('iphone')
    driver.implicitly_wait(6)

    # Step - 8 : Click search button
    element_locators = ["//input[@id='button-search' and @type='button']", '#button-search', '#button-search[type="button"]', 'input.btn', '#entry_212457 > div:nth-child(2) > div:nth-child(3) > input:nth-child(1)', "//input[starts-with(@type,'butto')]", "//input[contains(@class,'btn')]", "//input[contains(@type,'button')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 9 : Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 10 : Scroll 50% up in viewport
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight*0.5)")
    time.sleep(1)

    driver.quit()
except Exception as e:
    driver.quit()
