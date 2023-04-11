from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(1, "trybe", "eu", "26-09", "26-09", "123456", "aaaa")
    assert produto.id == 1
    assert produto.nome_da_empresa == "eu"
    assert produto.nome_do_produto == "trybe"
    assert produto.data_de_fabricacao == "26-09"
    assert produto.data_de_validade == "26-09"
    assert produto.numero_de_serie == "123456"
    assert produto.instrucoes_de_armazenamento == "aaaa"
