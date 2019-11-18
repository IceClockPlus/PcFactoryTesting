from behave import given,when,then
from webapp import webapp

driver = webapp.get_driver()

@given(u'Ingresa el producto a agregar "{producto}"')
def ingresar_el_producto_a_agregar(context,producto):
    driver.get("https://www.pcfactory.cl")

    elemen = driver.find_element_by_xpath("//*[@id='search']")
    elemen.clear()
    elemen.send_keys(producto)


@when(u'Buscamos el producto a agregar "{boton}"')
def buscar_producto_a_agregar(context,boton):
    driver.find_element_by_xpath(boton).click()

@when(u'Selecciona el producto a agregar')
def seleccionar_producto_a_agregar(context):
    driver.find_element_by_xpath("//*[@id='calugas-productos']/div/div[2]/a/div[1]/span[2]").click()


@when(u'Oprime en el boton de agregar el producto al carro de compra "{boton}"')
def oprimir_boton_para_agregar_producto_al_carro(context, boton):
    driver.find_element_by_xpath(boton).click()


@then(u'Se visualiza el producto en el carro de compra')
def visualiza_producto_en_carro_compra(context):
    productoCarro = driver.find_element_by_xpath("//*[@id='caluga_carro_26649']")
    assert productoCarro.is_displayed()
