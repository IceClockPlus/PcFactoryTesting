from behave import given,when,then
from selenium.webdriver.support.wait import WebDriverWait

from webapp import webapp

driver = webapp.get_driver()

@given(u'Acceder a la url "{url}" para iniciar la sesion')
def accede_url_para_iniciar_la_sesion(context,url):
    driver.get(url)

@when(u'Ingresar el rut "{valor}" en el campo Rut "{campo}" para iniciar')
def ingresar_el_rut_en_el_campo_para_iniciar(context,valor,campo):
    elemen = driver.find_element_by_xpath(campo)
    elemen.clear()
    elemen.send_keys(valor)

@when(u'Ingresar la clave "{valor}" en el campo clave "{campo}" para iniciar')
def ingresar_clave_en_el_campo_para_iniciar(context,valor,campo):
    elemen = driver.find_element_by_xpath(campo)
    elemen.clear()
    elemen.send_keys(valor)

@when(u'Iniciar sesion con el boton "{boton}"')
def iniciar_sesion_con_el_boton(context,boton):
    driver.find_element_by_xpath(boton).click()
    driver.implicitly_wait(3)

@when(u'Presionar el boton "{boton}" para cerrar sesion')
def presiona_boton_para_cerrar_sesion(context,boton):
    driver.find_element_by_xpath(boton).click()

@then(u'La sesion se cierra correctamente')
def la_sesion_cierra_correctamente(context):
    elemen = driver.find_element_by_xpath("//*[@id='id_login_off']")
    assert elemen.is_displayed()