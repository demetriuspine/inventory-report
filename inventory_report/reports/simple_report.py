from collections import Counter


class SimpleReport:

    def generate(products_list):
        production_date = []
        expiration_date = []
        companies = []
        for product in products_list:
            production_date.append(product["data_de_fabricacao"])
            companies.append(product["nome_da_empresa"])
            expiration_date.append(product["data_de_validade"])
        oldest_fabrication = min(production_date)
        min_validity = min(expiration_date)
        qnt_companies = Counter(companies)
        most_prod_company = qnt_companies.most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication}\n"
            f"Data de validade mais próxima: {min_validity}\n"
            f"Empresa com mais produtos: {most_prod_company}"
        )
