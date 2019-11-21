Feature: Inicio de Sesion
  Scenario: Iniciar Sesion
    Given Accede a la url "https://www.pcfactory.cl" para iniciar sesion
    When  Ingresar el rut "ingreseRut" en el campo Rut "//*[@id='rutId1']"
    And   Ingresar la clave "ingreseContraseña" en el campo clave "//*[@id='rutId2']"
    And   Presiona el boton para iniciar sesion "//*[@id='btn_login']"
    Then  Inicia sesion exitosamente

  Scenario: Iniciar Sesion Contrasenia Incorrecta
    Given Accede a la url "https://www.pcfactory.cl" para intentar iniciar sesion
    When  Ingresar correctamente el rut "ingreseRut" en el campo Rut "//*[@id='rutId1']"
    And   Ingresar la clave incorrecta "blackboard" en el campo clave "//*[@id='rutId2']"
    And   Presiona el boton para intentar iniciar sesion "//*[@id='btn_login']"
    Then  Muestra mensaje indicando credenciales incorrecta


  Scenario: Iniciar Sesion Rut Invalido
    Given Accede a la url "https://www.pcfactory.cl" para intentar iniciar sesion con rut invalido
    When  Ingresa el rut invalido "126635323" en el campo Rut "//*[@id='rutId1']"
    And   Ingresar la clave valida "blackboard" en el campo clave "//*[@id='rutId2']"
    And   Presionar el boton para intentar iniciar sesion con rut invalido "//*[@id='btn_login']"
    Then  Muestra mensaje de Rut invalido