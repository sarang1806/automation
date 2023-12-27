from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilitiy import config_reader,read_write_xl,db_function
import openpyxl
import unittest

@given(u'Open Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@given(u'Enter the Guru99 site url')
def step_impl(context):
    URL_guru= config_reader.Read_config("basic-info", "project_URL")
    context.driver.get(URL_guru)
    context.driver.maximize_window()
    context.driver.implicitly_wait(100)
    time.sleep(3)

@given(u'Enter user Id and password with role "{role}"')
def step_impl(context,role):
    flag = False
    username,password= db_function.get_credentials("manager")
    # username,passward = read_write_xl.get_username_password("common",role)
    if username.strip()=="" or password.strip()=="":
        flag = True
    if flag == False:

        user_guruName= config_reader.Read_config("basic-info", "user_NAME")
        context.driver.find_element(By.NAME, 'uid').send_keys(username)

        user_guruPass= config_reader.Read_config("basic-info", "password_NAME")
        context.driver.find_element(By.NAME, 'password').send_keys(password)

    else:
        unittest.TestCase.assertTrue(flag,"role does not match")


# @given(u'Enter password')
# def step_impl(context):

@then(u'Click on login button')
def step_impl(context):
    user_guruLogin= config_reader.Read_config("basic-info", "login_NAME")
    context.driver.find_element(By.NAME, 'btnLogin').click()
    time.sleep(3)

@then(u'Verify customer logged in successfully')
def step_impl(context):
    status = config_reader.Read_config("basic-info", "status_XPATH")
    status = context.driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[3]/td').is_displayed()
    assert status is True
