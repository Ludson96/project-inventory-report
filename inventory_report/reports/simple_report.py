from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def get_oldest_fabricacao(cls, items: list[dict]) -> str:
        datas_de_fabricacao = [
            datetime.strptime(item["data_de_fabricacao"], "%Y-%m-%d").date()
            for item in items
        ]
        return min(datas_de_fabricacao)

    @classmethod
    def get_newest_validade(cls, items: list[dict]) -> str:
        datas_de_validade = [
            datetime.strptime(item["data_de_validade"], "%Y-%m-%d").date()
            for item in items
            if datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        ]
        return min(datas_de_validade)

    @classmethod
    def quantity_product_empresas(cls, items: list[dict]) -> str:
        empresas = [item["nome_da_empresa"] for item in items]
        return Counter(empresas).most_common()[0][0]

    @classmethod
    def generate(cls, items: list[dict]) -> str:
        newest_de_validade = cls.get_newest_validade(items)
        oldest_fabricacao = cls.get_oldest_fabricacao(items)
        empresa_mais_frequente = cls.quantity_product_empresas(items)
        return (
            f"Data de fabricação mais antiga: {oldest_fabricacao}\n"
            f"Data de validade mais próxima: {newest_de_validade}\n"
            f"Empresa com mais produtos: {empresa_mais_frequente}"
        )
