Feature: Buscar Producto
Scenario: Buscar producto por nombre
    Given Accede a la url "www.pcfactory.cl"
    When  Ingreso en el campo busqueda "//*[@id='search']" el texto "CPU Core i5"
    And   Oprime el boton para buscar "//*[@id='search_btn']"
    Then  Muestra el listado con los productos coincidentes
