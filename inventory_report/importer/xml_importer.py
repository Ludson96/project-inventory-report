import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XMLImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" in path:
            tree = ET.parse(path)
            return tree.getroot()
        raise ValueError("Arquivo inválido")
