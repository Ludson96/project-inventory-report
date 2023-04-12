from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CSVImporter
from inventory_report.importer.json_importer import JSONImporter
from inventory_report.importer.xml_importer import XMLImporter


class Inventory:
    importers = {
        "csv": CSVImporter,
        "json": JSONImporter,
        "xml": XMLImporter,
    }
    reports = {"simples": SimpleReport, "completo": CompleteReport}

    @classmethod
    def import_data(cls, path, type):
        file_extension = path.split(".")[-1]
        reader = cls.importers[file_extension].import_data(path)
        return cls.reports[type].generate(reader)
