Feature: Buscar Producto
Scenario: Buscar producto por nombre
    Given Accede a la url "https://www.pcfactory.cl"
    When  Ingreso en el campo busqueda "//*[@id='search']" el texto "CPU Core i5"
    And   Oprime el boton para buscar "//*[@id='search_btn']"
    Then  Muestra el listado con los productos coincidentes

Scenario: Buscar producto por codigo
    Given Accede a la pagina "https://www.pcfactory.cl"
    When  Ingrese en el campo busqueda "//*[@id='search']" el codigo "29520"
    And   Oprima el boton para buscar "//*[@id='search_btn']"
    Then  Muestra en el listado el producto con el codigo ingresado


Scenario: Buscar producto inexistente
    Given Accede a la url "https://www.pcfactory.cl" para buscar producto inexistente
    When  Ingresa en el campo busqueda "//*[@id='search']" el producto inexistente "jyfc"
    And   Oprime el boton para intentar buscar "//*[@id='search_btn']"
    Then  Muestra el mensaje que indica la inexistencia del producto