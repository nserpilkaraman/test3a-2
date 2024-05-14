import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from test_automation_odev import globalConstants

class Test_invalidLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get(globalConstants.BASE_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_invalidLogin(self):
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, globalConstants.username_id)))
    self.driver.find_element(By.ID, globalConstants.username_id).send_keys("1")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, globalConstants.password_id)))
    self.driver.find_element(By.ID, globalConstants.password_id).send_keys("1")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, globalConstants.login_button_id)))
    self.driver.find_element(By.ID, globalConstants.login_button_id).click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required"