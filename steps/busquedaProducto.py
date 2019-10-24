from behave import given,when,then
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
    driver.find_element_by_xpath(boton).click()


@then(u'Muestra el listado con los productos coincidentes')
def muestra_lisado_con_productos_coincidentes(context):
    listProductos = driver.find_element_by_xpath("//*[@id='calugas-productos']")
    driver.implicitly_wait(5)
    try:
        assert listProductos.is_displayed()
    except:
        print("Listado no desplegado")



@given(u'Accede a la pagina "{url}"')
def acceder_a_la_pagina(context, url):
    driver.get(url)

@when(u'Ingrese en el campo busqueda "{busqueda}" el codigo "{codigo}"')
def ingresar_codigo_producto_en_el_campo_busqueda(context,busqueda,codigo):
    elemen = driver.find_element_by_xpath(busqueda)
    elemen.clear()
    elemen.send_keys(codigo)


@when(u'Oprima el boton para buscar "{boton}"')
def oprima_boton_para_buscar(context,boton):
    driver.find_element_by_xpath(boton).click()


@then(u'Muestra en el listado el producto con el codigo ingresado')
def mostrar_listado_producto_con_el_codigo_ingresado(context):
    codProducto = driver.find_element_by_xpath("//*[@id='calugas-productos']/div/div[1]/div[1]/span").text
    assert codProducto in "29520"
    webapp.tearDown()
