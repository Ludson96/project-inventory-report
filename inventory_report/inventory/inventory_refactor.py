from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type) -> list[dict]:
        data = self.importer.import_data(path)
        for item in data:
            self.data.append(item)

        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)

    def __iter__(self) -> list[dict]:
        return InventoryIterator(self.data)
