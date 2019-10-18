Feature: Buscar Producto por Categoria
Scenario: Buscar Producto por Categoria
    Given Accede a la url "www.pcfactory.cl"
    When  Ingreso en el campo busqueda "//*[@id='search']" el texto "CPU Core i5"
    When  Hacer click en Todas Las Categorias "//*[@id="drop-down-content]" la imagen "img"