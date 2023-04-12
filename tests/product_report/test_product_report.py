from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "123",
        "ao abrigo de luz",
    )

    srt_product = product.__repr__()

    frase = (
        "O produto farinha fabricado em 01-05-2021 por Farinini "
        "com validade até 02-06-2023 precisa ser armazenado ao abrigo de luz."
    )

    assert frase == srt_product
