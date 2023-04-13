from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []
        self.reports = {"simples": SimpleReport, "completo": CompleteReport}

    def import_data(self, path, report_type) -> list[dict]:
        data = self.importer.import_data(path)
        for item in data:
            self.data.append(item)

        return self.reports[report_type].generate(data)

    def __iter__(self) -> list[dict]:
        return InventoryIterator(self.data)
