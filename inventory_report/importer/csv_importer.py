from inventory_report.importer.importer import Importer
import csv


class CSVImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" in path:
            with open(path, mode="r") as file:
                reader = csv.DictReader(file, delimiter=",", quotechar='"')
                return list(reader)
        raise ValueError("Arquivo inválido")
