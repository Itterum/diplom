import re

from openpyxl import load_workbook
from dataclasses import dataclass, field
from typing import List

from openpyxl.worksheet.worksheet import Worksheet


@dataclass
class TemplateDay:
    date: str = ""
    teacher: str = ""
    discipline: str = ""
    department: str = ""
    type: str = ""
    visit: str = ""
    para: str = ""
    session: bool = None


@dataclass
class TemplateGroup:
    group_id: int = 0
    days: List[TemplateDay] = field(default_factory=list)


class ParseXlsx:
    def __init__(self, path: str) -> None:
        self.worksheet = None
        self.path: str = path
        self.worksheet: Worksheet

    def open_file(self) -> None:
        self.worksheet = load_workbook(self.path).active

    def parse(self) -> list[TemplateGroup]:
        self.open_file()
        table = self._parse_column()
        return table

    def _parse_column(self) -> list:
        table = []
        for col in self.worksheet.columns:
            for item in self._parse_cell(col):
                table.append(item)
        return table

    def _parse_cell(self, col) -> list:
        group = TemplateGroup()
        day = TemplateDay()
        date = None
        for cell in col:
            if cell.value is None:
                continue

            data = self.get_data_cell(cell)

            if data[0] == "para":
                if day.para != '':
                    group.days.append(day)
                    day = TemplateDay()

            if data[0] == "group":
                if group.group_id != 0:
                    yield group
                    group = TemplateGroup()
                group.group_id = data[1]

            if data[0] == "date":
                date = data[1]

            setattr(day, *self.handler_data(data, date, day))
        else:
            if group.group_id != 0:
                yield group

    def handler_data(self, data: list, date: str, day: TemplateDay) -> tuple:
        if getattr(day, "date", False) == "":
            return "date", date
        return data[0], data[1]

    @staticmethod
    def get_data_cell(cell) -> list:
        return re.split(r":\s", cell.value)
