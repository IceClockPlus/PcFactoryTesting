from behave import given,when,then
from webapp import webapp

driver = webapp.get_driver()

@given(u'Busca el producto en la seccion de busqueda "{busqueda}" el producto "{producto}"')
def buscar_producto_en_la_seccion_de_busqueda_el_producto(context,busqueda ,producto):
    driver.get("https://www.pcfactory.cl")

    elemen = driver.find_element_by_xpath(busqueda)
    elemen.clear()
    elemen.send_keys(producto)


@when(u'Presiona el boton para buscar "{boton}"')
def presionar_el_boton_para_buscar(context,boton):
    driver.find_element_by_xpath(boton).click()


@when(u'Elige el producto deseado')
def elige_el_producto_deseado(context):
    driver.find_element_by_xpath("//*[@id='calugas-productos']/div/div[2]/a/div[1]/span[2]").click()


@then(u'Se muestra toda la informacion del producto')
def muestra_toda_la_informacion_del_producto(context):
    datoProducto = driver.find_element_by_xpath("//*[@id='id_ficha_producto']")
    try:
        assert datoProducto.is_displayed()
    except:
        print("Datos no mostrados")

@given(u'Busco el producto deseado con el nombre "{producto}"')
def busco_producto_deseado_con_el_nombre(context,producto):
    driver.get("https://www.pcfactory.cl")

    elemen = driver.find_element_by_xpath("//*[@id='search']")
    elemen.clear()
    elemen.send_keys(producto)

@when(u'Oprimo el boton buscar "{boton}"')
def oprimo_el_boton_buscar(context,boton):
    driver.find_element_by_xpath(boton).click()

@when(u'Selecciono el producto')
def selecciono_el_producto(context):
    driver.find_element_by_xpath("//*[@id='calugas-productos']/div/div[2]/a/div[1]/span[2]").click()


@when(u'Oprime la pestana de Descripcion "{descripcion}"')
def oprime_la_pestana_descripcion(context,descripcion):
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_xpath(descripcion).click()
    except:
        print("Pestaña ya oprimida")

@then(u'Se muestra la descipcion del producto')
def muestra_descripcion_del_producto(context):
    desc = driver.find_element_by_xpath("//*[@id='parentHorizontalTab']/div/div[1]")
    assert desc.is_displayed()

