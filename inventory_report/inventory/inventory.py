from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    importers = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }
    reports = {"simples": SimpleReport, "completo": CompleteReport}

    @classmethod
    def import_data(cls, path, type):
        file_extension = path.split(".")[-1]
        reader = cls.importers[file_extension].import_data(path)
        return cls.reports[type].generate(reader)
