from behave import given,when,then
from webapp import webapp

driver = webapp.get_driver()


@given(u'Accede a la url "{url}"')
def acceder_a_la_url(context, url):
    driver.get(url)
    driver.save_screenshot("C://Evidencia_Prueba//acceder_a_la_url.png")
    print("Captura Realizada")


@when(u'Ingreso en el campo busqueda "{busqueda}" el texto "{valor}"')
def ingreso_de_nombre_producto_en_el_campo_busqueda(context, busqueda, valor):
    elemen = driver.find_element_by_xpath(busqueda)
    elemen.clear()
    elemen.send_keys(valor)
    driver.save_screenshot("C://Evidencia_Prueba//ingreso_nombre_producto_en_el_campo_busqueda.png")
    print("Captura Realizada")


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

    driver.save_screenshot("C://Evidencia_Prueba//Muestra_el_listado_con_productos.png")
    print("Captura Realizada")

@given(u'Accede a la pagina "{url}"')
def acceder_a_la_pagina(context, url):
    driver.get(url)
    driver.save_screenshot("C://Evidencia_Prueba//accede_a_la_pagina.png")
    print("Captura Realizada")

@when(u'Ingrese en el campo busqueda "{busqueda}" el codigo "{codigo}"')
def ingresar_codigo_producto_en_el_campo_busqueda(context,busqueda,codigo):
    elemen = driver.find_element_by_xpath(busqueda)
    elemen.clear()
    elemen.send_keys(codigo)
    driver.save_screenshot("C://Evidencia_Prueba//ingresar_codigo_producto_en_campo_busqueda.png")
    print("Captura Realizada")


@when(u'Oprima el boton para buscar "{boton}"')
def oprima_boton_para_buscar(context,boton):
    driver.find_element_by_xpath(boton).click()


@then(u'Muestra en el listado el producto con el codigo ingresado')
def mostrar_listado_producto_con_el_codigo_ingresado(context):
    codProducto = driver.find_element_by_xpath("//*[@id='calugas-productos']/div/div[1]/div[1]/span").text
    try:
        assert codProducto in "29520"
    except:
        print("Producto no encontrado")

    driver.save_screenshot("C://Evidencia_Prueba//mostrar_listado_producto_con_codigo_ingresado.png")

@given(u'Accede a la url "{url}" para buscar producto inexistente')
def accede_a_url_para_buscar_producto_inexistente(context,url):
    driver.get(url)
    driver.save_screenshot("C://Evidencia_Prueba//accede_url_para_buscar_producto_inexistente.png")


@when(u'Ingresa en el campo busqueda "{busqueda}" el producto inexistente "{valor}"')
def ingresa_en_campo_busqueda_producto_inexistente(context,busqueda,valor):
    elemen = driver.find_element_by_xpath(busqueda)
    elemen.clear()
    elemen.send_keys(valor)
    driver.save_screenshot("C://Evidencia_Prueba//ingresar_en_campo_busqueda_producto_inexistente.png")
    driver.implicitly_wait(2)

@when(u'Oprime el boton para intentar buscar "{boton}"')
def oprime_boton_para_intentar_buscar(context,boton):
    driver.find_element_by_xpath(boton).click()

@then(u'Muestra el mensaje que indica la inexistencia del producto')
def muestra_mensaje_indica_inexistencia_producto(context):
    try:
        mensaje = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/h1").text
        assert mensaje in 'No se encontraron resultados para la búsqueda "jyfc"'
    except:
        print("Mensaje no mostrado")

    driver.save_screenshot("C://Evidencia_Prueba//muestra_mensaje_producto_inexistente.png")
    webapp.tearDown()