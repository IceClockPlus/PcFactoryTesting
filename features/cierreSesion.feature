Feature: Cierre de Sesion
  Scenario: Cerrar Sesion
    Given Acceder a la url "https://www.pcfactory.cl" para iniciar la sesion
    When  Ingresar el rut "ingreseRut" en el campo Rut "//*[@id='rutId1']" para iniciar
    And   Ingresar la clave "ingreseContraseña" en el campo clave "//*[@id='rutId2']" para iniciar
    And   Iniciar sesion con el boton "//*[@id='btn_login']"
    And   Presionar el boton "//*[@id='id_mi_cerrar_session']" para cerrar sesion
    Then  La sesion se cierra correctamente