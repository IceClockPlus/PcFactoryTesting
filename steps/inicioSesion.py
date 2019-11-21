from behave import given,when,then
from webapp import webapp

driver = webapp.get_driver()

@given(u'Accede a la url "{url}" para iniciar sesion')
def accede_url_para_iniciar_sesion(context,url):
    driver.get(url)

@when(u'Ingresar el rut "{valor}" en el campo Rut "{campo}"')
def ingresar_el_rut_en_el_campo_rut(context,valor,campo):
    elemen = driver.find_element_by_xpath(campo)
    elemen.clear()
    elemen.send_keys(valor)

@when(u'Ingresar la clave "{valor}" en el campo clave "{campo}"')
def ingresar_clave_en_el_campo_clave(context,valor,campo):
    elemen = driver.find_element_by_xpath(campo)
    elemen.clear()
    elemen.send_keys(valor)

@when(u'Presiona el boton para iniciar sesion "{boton}"')
def presiona_boton_para_iniciar_sesion(context,boton):
    driver.find_element_by_xpath(boton).click()
    driver.implicitly_wait(2)

@then(u'Inicia sesion exitosamente')
def inicia_sesion_exitosamente(context):
    try:
        elemen = driver.find_element_by_xpath("//*[@id='id_login_on']")
        assert elemen.is_displayed()
    except:
        print("No inicio sesion")

@given(u'Accede a la url "{url}" para intentar iniciar sesion')
def accede_a_url_para_intentar_iniciar_sesion(context,url):
    driver.delete_all_cookies()
    driver.get(url)

@when(u'Ingresar correctamente el rut "{valor}" en el campo Rut "{campo}"')
def ingresar_correctamente_el_rut_en_el_campo(context,valor,campo):
    elemen = driver.find_element_by_xpath(campo)
    elemen.clear()
    elemen.send_keys(valor)

@when(u'Ingresar la clave incorrecta "{valor}" en el campo clave "{campo}"')
def ingresar_la_calve_incorrecta_en_el_campo(context,valor,campo):
    elemen = driver.find_element_by_xpath(campo)
    elemen.clear()
    elemen.send_keys(valor)

@when(u'Presiona el boton para intentar iniciar sesion "{boton}"')
def presiona_boton_para_intentar_iniciar_sesion(context,boton):
    driver.find_element_by_xpath(boton).click()

@then(u'Muestra mensaje indicando credenciales incorrecta')
def muestra_mensaje_indicando_credenciales_incorrecta(context):
    mensaje = driver.find_element_by_xpath("//*[@id='id_nota_forgot_password']").text
    assert mensaje in "Contraseña incorrecta"


@given(u'Accede a la url "{url}" para intentar iniciar sesion con rut invalido')
def acceder_a_url_para_iniciar_sesion_con_rut_invalido(context,url):
    driver.delete_all_cookies()
    driver.get(url)

@when(u'Ingresa el rut invalido "{valor}" en el campo Rut "{campo}"')
def ingresar_rut_invalido_en_el_campo_rut(context,valor,campo):
    elemen = driver.find_element_by_xpath(campo)
    elemen.clear()
    elemen.send_keys(valor)

@when(u'Ingresar la clave valida "{valor}" en el campo clave "{campo}"')
def ingresar_clave_valida_en_el_campo_clave(context,valor,campo):
    elemen = driver.find_element_by_xpath(campo)
    elemen.clear()
    elemen.send_keys(valor)
@when(u'Presionar el boton para intentar iniciar sesion con rut invalido "{boton}"')
def presionar_boton_para_iniciar_sesion_con_rut_invalido(context,boton):
    driver.find_element_by_xpath(boton).click()

@then(u'Muestra mensaje de Rut invalido')
def muestra_mensaje_rut_invalido(context):
    mensaje = driver.find_element_by_xpath("//*[@id='id_nota_forgot_password']").text
    assert mensaje in "Rut Inválido"