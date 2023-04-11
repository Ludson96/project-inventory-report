from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(items):
        datas_de_fabricacao = [
            datetime.strptime(item["data_de_fabricacao"], "%Y-%m-%d").date()
            for item in items
        ]
        oldest_fabricacao = min(datas_de_fabricacao)

        datas_de_validade = [
            datetime.strptime(item["data_de_validade"], "%Y-%m-%d").date()
            for item in items
            if datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        ]
        newest_de_validade = min(datas_de_validade)

        empresas = {}
        for item in items:
            empresa = item["nome_da_empresa"]
            if empresa in empresas:
                empresas[empresa] += 1
            else:
                empresas[empresa] = 1

        empresa_mais_frequente = max(empresas, key=empresas.get)

        return (
            f"Data de fabricação mais antiga: {oldest_fabricacao}\n"
            f"Data de validade mais próxima: {newest_de_validade}\n"
            f"Empresa com mais produtos: {empresa_mais_frequente}"
        )
