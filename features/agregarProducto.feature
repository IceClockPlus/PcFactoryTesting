Feature: Agregar al carro
  Scenario: Agregar un producto al carro
    Given Ingresa el producto a agregar "Wind blade 120 blue"
    When Buscamos el producto a agregar "//*[@id='search_btn']"
    And  Selecciona el producto a agregar
    And Oprime en el boton de agregar el producto al carro de compra "//*[@id='agrega_carro']"
    Then Se visualiza el producto en el carro de compra

