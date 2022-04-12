from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(8)
driver.get("https://www.knyguklubas.lt/literatura-vaikams?product_list_limit=96&product_list_order=most_reviews")

# Get the list of authors of children literature

button = driver.find_element(
    By.XPATH, '/html/body/div[3]/div[3]/div[1]/div/div[2]/div/div/div/div/div[1]/a')
button.click()

full_list = []
authors = driver.find_elements(
    By.XPATH, '/html/body/div[2]/main/div[4]/div[1]/div[3]/div[3]/ol/li/div/div[2]/div[1]/p')
for author in authors:
    full_list.append(author.text)

next = driver.find_element(
    By.XPATH, '/html/body/div[2]/main/div[4]/div[1]/div[3]/div[4]/div[2]/ul/li[6]')
next.click()

authors = driver.find_elements(
    By.XPATH, '/html/body/div[2]/main/div[5]/div[1]/div[3]/div[3]/ol/li/div/div[2]/div[1]/p')
for author in authors:
    full_list.append(author.text)

full_list_no_na = [value for value in full_list if value != 'Nėra Autoriaus']


# Get the list of top authors from 2019

name_author = '/html/body/div[2]/main/div[3]/div/div[2]/div[2]/div[4]/div[1]/ol/li/div/div[2]/div[1]/p'

driver.get("https://www.knyguklubas.lt/2019-uju-top-100?pyaavi=1")
authors_2019 = []

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((
    By.XPATH, name_author)))

authors_1 = driver.find_elements(
    By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div[2]/div[4]/div[1]/ol/li/div/div[2]/div[1]/p')
for author in authors_1:
    authors_2019.append(author.text)

driver.get("https://www.knyguklubas.lt/2019-uju-top-100?pyaavi=2")
element = wait.until(EC.element_to_be_clickable((
    By.XPATH, name_author)))

authors_2 = driver.find_elements(
    By.XPATH, name_author)

for author in authors_2:
    authors_2019.append(author.text)


# Get the list of top authors from 2021
driver.get("https://www.knyguklubas.lt/populiariausios-metu-knygos")

authors_2021 = []
element = wait.until(EC.element_to_be_clickable((
    By.XPATH, '/html/body/div[2]/main/div[4]/div[1]/div[2]/div[2]/div[4]/div[1]/ol/li/div/div[2]/div[1]/p')))

authors_wb = driver.find_elements(
    By.XPATH, '/html/body/div[2]/main/div[4]/div[1]/div[2]/div[2]/div[4]/div[1]/ol/li/div/div[2]/div[1]/p')

for author in authors_wb:
    authors_2021.append(author.text)

children_author_2019 = []
children_author_2021 = []

for author in full_list_no_na:
    if author in authors_2019:
        children_author_2019.append(author)
        print(author)
    if author in authors_2021:
        children_author_2021.append(author)
        print(author)

print(f"There are a total of {len(children_author_2019)} children literature books in the list of most popular books. On a total of {len(authors_2019)} books.")
print(f"There are a total of {len(children_author_2021)} children literature books in the list of most popular books. On a total of {len(authors_2021)} books.")
