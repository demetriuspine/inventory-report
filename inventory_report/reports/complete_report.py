from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(products):
        companies = []
        for product in products:
            companies.append(product["nome_da_empresa"])

        stock_message = ""
        for company in Counter(companies).items():
            stock_message += f"- {company[0]}: {company[1]}\n"

        return (
            f"{SimpleReport.generate(products)}\n"
            f"Produtos estocados por empresa:\n"
            f"{stock_message}"
        )
