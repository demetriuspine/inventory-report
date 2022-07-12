import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def csv_file(path):
        list_from_inventory = []
        with open(path) as file:
            for row in csv.DictReader(file):
                list_from_inventory.append(row)
        file.close()
        return list_from_inventory

    def json_file(path):
        with open(path) as file:
            list_from_inventory = json.load(file)
        file.close()
        return list_from_inventory

    def xml_file(path):
        list_from_inventory = []
        with open(path) as file:
            for row in xmltodict.parse(file.read())["dataset"]["record"]:
                list_from_inventory.append(row)
        file.close()
        return list_from_inventory

    @classmethod
    def import_data(self, path, report):
        list_from_inventory = []
        if ".csv" in path:
            list_from_inventory = self.csv_file(path)
        elif ".json" in path:
            list_from_inventory = self.json_file(path)
        elif ".xml" in path:
            list_from_inventory = self.xml_file(path)
        if report == "simples":
            simple_report = SimpleReport.generate(list_from_inventory)
            return simple_report
        else:
            complete_report = CompleteReport.generate(list_from_inventory)
            return complete_report
