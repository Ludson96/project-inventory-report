from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, items: list[dict]) -> str:
        simple_report = super().generate(items)
        all_empresas = [item["nome_da_empresa"] for item in items]
        quantity_product = Counter(all_empresas)
        relation_empresa_quantidade = [
            f"- {empresa}: {quantidade}\n"
            for empresa, quantidade in quantity_product.items()
        ]

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{''.join(relation_empresa_quantidade)}"
        )
