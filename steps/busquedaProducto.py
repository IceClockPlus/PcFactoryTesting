from behave import *
from webapp import webapp

driver = webapp.get_driver()


@given(u'Accede a la url "{url}"')
def acceder_a_la_url(context, url):
    driver.get(url)


@when(u'Ingreso en el campo busqueda "{busqueda}" el texto "{valor}"')
def ingreso_de_nombre_producto_en_el_campo_busqueda(context, busqueda, valor):
    elemen = driver.find_element_by_xpath(busqueda)
    elemen.clear()
    elemen.send_keys(valor)


@when(u'Oprime el boton para buscar "{boton}"')
def oprimir_boton_para_buscar(context, boton):
    driver.find_element_element_by_xpath(boton).click()


@then(u'Muestra el listado con los productos coincidentes')
def muestra_lisado_con_productos_coincidentes(context):
    count = len(driver.find_element_by_xpath("//*[@id='calugas-productos']/div"))
    print(count)
    webapp.tearDown()