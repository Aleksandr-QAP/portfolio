import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import Counter

driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/chromedriver.exe')
   pytest.driver.get('http://petfriends1.herokuapp.com/login')
   pytest.driver.find_element_by_id('email').send_keys('login')
   pytest.driver.find_element_by_id('pass').send_keys('password')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   pytest.driver.find_element_by_xpath('/html/body/nav/button/span').click()
   pytest.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[1]/a').click()


   yield

   pytest.driver.quit()


def test_find_all_pets():
   cards_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr")))
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[1]")))
   number_of_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]"))).text
   number_of_pets = number_of_pets.split()
   number_of_pets = int(number_of_pets[3])
   names_of_pet=[]
   for i in range(len(names)):
      assert names[i].text != ''
      names_of_pet.append(names[i].text)
   assert number_of_pets == len(cards_pets)

def test_half_of_the_pets_includes_photo():

   number_of_pets= WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]"))).text
   number_of_pets=number_of_pets.split()
   number_of_pets=int(number_of_pets[3])

   images=WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/th/img")))
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[1]")))

   photo=[]

   for i in range(len(names)):

      photo.append(images[i].get_attribute('src'))

   photo = Counter(photo)
   assert photo[''] < number_of_pets / 2



def test_all_pets_includes_name_age_type():
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[1]")))
   age = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[3]")))
   breed = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[2]")))

   for i in range(len(names)):
      assert names[i].text != ''
      assert age[i].text != ''
      assert breed[i].text != ''

def test_various_name_of_the_pets():
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[1]")))
   names_of_pet = []
   for i in range(len(names)):
      names_of_pet.append(names[i].text)
   iterance = Counter(names_of_pet)
   for key in iterance:
      assert iterance[key] == 1

def test_no_iterants_pets_in_the_list():
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[1]")))
   age = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[3]")))
   breed = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[2]")))

   names_of_pet = []
   for i in range(len(names)):
      names_of_pet.append(names[i].text)
   iterance_names = Counter(names_of_pet)
   for key in iterance_names:
      assert iterance_names[key] == 1

   ages_of_pet = []
   for i in range(len(names)):
      ages_of_pet.append(age[i].text)
   iterance_ages = Counter(ages_of_pet)
   for key in iterance_ages:
      assert iterance_ages[key] == 1

   breeds_of_pet = []
   for i in range(len(names)):
      breeds_of_pet.append(breed[i].text)
   iterance_breeds = Counter(breeds_of_pet)
   for key in iterance_breeds:
      assert iterance_breeds[key] == 1

