import re

from openpyxl import load_workbook
from dataclasses import dataclass, asdict
from typing import List, Union

from openpyxl.worksheet.worksheet import Worksheet


@dataclass
class TemplateDay:
    group: str = ""
    date: str = ""
    teacher: str = ""
    discipline: str = ""
    department: str = ""
    type: str = ""
    visit: str = ""
    para: str = ""
    session: bool = None


class ParseXlsx:
    def __init__(self, path: str) -> None:
        self.worksheet = None
        self.path: str = path
        self.worksheet: Worksheet

    def open_file(self) -> None:
        self.worksheet = load_workbook(self.path).active

    def parse(self, to_dict: bool = False) -> Union[List[TemplateDay], dict]:
        self.open_file()
        table = self._parse_column(to_dict=to_dict)
        return table

    def _parse_column(self, to_dict: bool = False) -> List:
        table = []
        for col in self.worksheet.columns:
            for item in self._parse_cell(col):
                if to_dict:
                    item = asdict(item)
                table.append(item)
        return table

    def _parse_cell(self, col) -> List:
        day = TemplateDay()
        date = None
        group = 0
        for cell in col:
            if cell.value is None:
                continue

            data = self.get_data_cell(cell)

            if data[0] == "para":
                if day.group != "" and day.para != "":
                    yield day
                    day = TemplateDay()
                day.group = group
                day.para = data[1]
                day.date = date

            if data[0] == "group":
                group = data[1]

            if data[0] == "date":
                date = data[1]

            setattr(day, *self.handler_data(data, date, group, day))
        else:
            if day.group != "" and day.para != "":
                yield day

    def handler_data(self, data: list, date: str, group: str, day: TemplateDay) -> tuple:
        if getattr(day, "date", False) == "":
            return "date", date
        if getattr(day, "group", False) == "":
            return "group", group
        return data[0], data[1]

    @staticmethod
    def get_data_cell(cell) -> List:
        return re.split(r":\s", cell.value)
