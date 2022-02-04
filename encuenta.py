from selenium  import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

# Le pasamos la dirección donde descargamos nuestro driver
driver = webdriver.Chrome(executable_path='/Users/os/Desktop/encuenta/chromedriver 2')

# Le pasamos la URL del sitio que vamos a automatizar
driver.get('https://rrhh.claro.com.ni:8443/')


input_pais = driver.find_element_by_xpath("/html/body/form/div/select") 
driver.implicitly_wait(10)
input_pais.send_keys('Nicaragua')


input_nombre = driver.find_element_by_xpath("/html/body/form/div/input[1]") 
driver.implicitly_wait(10)
input_nombre.send_keys('500454')

input_password = driver.find_element_by_xpath("/html/body/form/div/input[2]") 
driver.implicitly_wait(10)
input_password.send_keys('Mayo2021')

driver.find_element_by_css_selector("#btnEntrar > div").click()

###before start session
driver.implicitly_wait(100)
#work
driver.find_element_by_css_selector("#rbOficina").click()

##no
driver.find_element_by_css_selector("#no").click()

##sintomas
driver.find_element_by_css_selector("#chkNinguno").click()

##covid
driver.find_element_by_css_selector("#rbNo").click()

#15 days
driver.find_element_by_xpath("/html/body/div/section/div/form/fieldset/fieldset[5]/div[2]/label/input").click()

#last
driver.find_element_by_css_selector("#chkMascarilla").click()

driver.find_element_by_css_selector("#chkAlcohol").click()

#save
driver.find_element_by_css_selector("#btnSave").click()



