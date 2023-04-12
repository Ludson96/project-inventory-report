import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XMLImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" in path:
            with open(path, mode="r") as file:
                tree = ET.parse(file)
                root = tree.getroot()
                data = []
                for item in root:
                    item_data = {}
                    for element in item:
                        item_data[element.tag] = element.text
                    data.append(item_data)
                return data
        raise ValueError("Arquivo inválido")
