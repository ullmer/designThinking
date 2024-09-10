#https://github.com/Kalmat/PyWinCtl
#https://www.selenium.dev/documentation/webdriver/interactions/windows/
#https://www.seleniumeasy.com/python/getting-started-selenium-webdriver-using-python
#https://selenium-python.readthedocs.io/getting-started.html

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.python.org")
driver.set_window_size(600, 600)
driver.set_window_position(0, 0)

#driver = webdriver.Firefox(executable_path='.\geckodriver.exe')

### end ###
