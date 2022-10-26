import unittest
import utils as Utils
import time
from selenium.webdriver.common.by import By


class Test_Selenium(unittest.TestCase):

    # Run specifified test:
    # pytest conceptoFacturable/testing/test_selenium.py -k 'test_detail'
    def test_detail(self):

        driver = Utils.setup_chrome()

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)
        Utils.go_to_element(driver, "6")

        element_present = driver.find_element("name", "card_header")
        time.sleep(2)
        assert element_present, "Concepto Test - Detalle"

    def test_create(self):

        driver = Utils.setup_chrome()

        button = driver.find_element("name", "create_button")
        button.click()

        # Form
        comunication_type = driver.find_element("name", "tipo_comunicacion")
        Utils.slow_typing(
            comunication_type,
            'ComunicacionTest')

        concept = driver.find_element("name", "concepto")
        Utils.slow_typing(
            concept,
            'ConceptTest')

        concept_class = driver.find_element("name", "clase_concepto")
        Utils.slow_typing(
            concept_class,
            'ConceptClassTest')

        operator_concept = driver.find_element("name", "concepto_operador")
        Utils.slow_typing(
            operator_concept,
            'OperatorConceptTest')

        operator = driver.find_element("name", "operador")
        Utils.slow_typing(
            operator,
            'OperatorTest')

        scope = driver.find_element("name", "ambito")
        Utils.slow_typing(
            scope,
            'ScopeTest')

        button = driver.find_element("name", "save_button")
        button.click()

        time.sleep(2)
        element_present = driver.find_element("name", "card_header")
        time.sleep(2)
        assert element_present, "ConceptTest_Selenium - Detalle"

    def test_login(self):
        driver = Utils.setup_chrome()
        driver.get("http://localhost:8000/admin/")
        time.sleep(2)
        username = driver.find_element("name", "username")
        Utils.slow_typing(
            username,
            'marcos')
        password = driver.find_element("name", "password")
        Utils.slow_typing(
            password,
            'Hola12345')
        driver.find_element(By.TAG_NAME, 'input').submit()
        time.sleep(2)

    def test_update(self):
        driver = Utils.setup_chrome()
        Utils.go_to_element(driver, "2")

        driver.find_element("name", "update_button").click()

        time.sleep(2)

        Utils.login(driver)

        driver.get("http://localhost:8000/conceptos/")
        time.sleep(2)

        Utils.go_to_element(driver, "2")

        time.sleep(2)
        driver.find_element("name", "update_button").click()
        time.sleep(2)
        input_field = driver.find_element("name", "tipo_comunicacion")
        input_field.clear()
        Utils.slow_typing(
            input_field,
            'testing_update')

        save_button = driver.find_element("name", "save_button")
        save_button.click()
        time.sleep(2)

    def test_delete(self):
        driver = Utils.setup_chrome()
        Utils.go_to_element(driver, "12")

        driver.find_element("name", "delete_button").click()

        Utils.login(driver)

        driver.get("http://localhost:8000/conceptos/")
        time.sleep(2)

        Utils.go_to_element(driver, "12")
        time.sleep(2)
        driver.find_element("name", "delete_button").click()
