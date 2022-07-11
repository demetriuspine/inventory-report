from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Les Paul",
        "Gibson",
        "1952-01-01",
        "2052-01-01",
        "09031997",
        "away from the sun",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Les Paul"
    assert product.nome_da_empresa == "Gibson"
    assert product.data_de_fabricacao == "1952-01-01"
    assert product.data_de_validade == "2052-01-01"
    assert product.numero_de_serie == "09031997"
    assert product.instrucoes_de_armazenamento == "away from the sun"
