from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" in path:
            with open(path, mode="r") as file:
                reader = json.load(file)
                return reader
        raise ValueError("Arquivo inválido")
