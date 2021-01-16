from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

element = browser.find_element_by_xpath("//button[@aria-label='Play']")
element.click()