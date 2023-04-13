import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) <= 2:
        return print("Verifique os argumentos", file=sys.stderr)

    importers = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }

    _, path, report_type = sys.argv

    file_extension = path.split(".")[-1]
    report = InventoryRefactor(importers[file_extension])
    reader = report.import_data(path, report_type)

    print(reader, end="")
