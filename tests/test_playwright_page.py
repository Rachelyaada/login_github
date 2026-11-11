from selenium.webdriver.common.by import By
import pytest

def test_playwright_page(driver):
    driver.get("https://playwright.dev/")
    try:
      driver.find_element(By.ID, "h1")
        # print(f"my_element: {my_element}")
    except :
        print("Element with ID 'h1' not found.")

    my_element = driver.find_element(By.ID, "h1")
    print(f"my_element: {my_element[0]}")
    # myelements= driver.find_elements(By.TAG_NAME, "h1")
    # print(f"myelements: {myelements}")
    # inputs = driver.find_elements(By.TAG_NAME, "input")
    
    # print(len(inputs))
    