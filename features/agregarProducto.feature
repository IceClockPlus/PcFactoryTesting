Feature: Agregar al carro
  Scenario: Agregar un producto al carro
    Given Buscamos el producto deseado a comprar de nombre "Wind blade 120 blue"
    When Selecciona el producto buscado
    And Oprime en el boton de agregar al carro
    Then Se visualiza el producto en el carro de compra

