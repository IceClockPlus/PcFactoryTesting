Feature: Despliegue de Producto
  Scenario: Seleccionar Producto
    Given Busca el producto en la seccion de busqueda "//*[@id='search']" el producto "Wind blade 120 blue"
    When  Presiona el boton para buscar "//*[@id='search_btn']"
    And   Elige el producto deseado
    Then  Se muestra toda la informacion del producto

  Scenario: Mostrar Descripcion de Producto
      Given Busco el producto deseado con el nombre "Wind blade 120 blue"
      When Oprimo el boton buscar "//*[@id='search_btn']"
      And Selecciono el producto
      And Oprime la pestana de Descripcion "//*[@id="parentHorizontalTab"]/ul/li[1]"
      Then Se muestra la descipcion del producto

