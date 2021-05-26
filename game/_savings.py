import operator
import functools

from game import Field
from game.player import Cell
from game.utils import FILE_TEMPLATE


def save(self):
    with open(FILE_TEMPLATE["saves_file"], "w") as file:
        for i in self._fields:
            for j in range(len(i.cells)):
                for k in range(len(i.cells[j])):
                    file.write(f"{i.cells[j][k].__hash__()} ")
                file.write("\n")
            file.write("===\n")


def restore(self):
    with open(FILE_TEMPLATE["saves_file"], "r") as file:
        lines: list[str] = file.readlines()

        string = functools.reduce(operator.add, lines, "")

        fields_str = string.split("==\n")

        hashed_cells: list[list[list[int]]] = \
            list(
                map(
                    lambda x:
                        list(
                            map(
                                lambda y:
                                    list(
                                        map(
                                            lambda z: int(z),
                                            y.split(" ")
                                        )
                                    ),
                                x.split("\n")
                            )
                        ),
                    fields_str
                )
            )

        fields: list[Field] = list(map(
            lambda x: Field(x["size"][0], x["size"][1], x["position"][0], x["position"][1]),
            [
                FILE_TEMPLATE["fields"][0],
                FILE_TEMPLATE["fields"][1],
                FILE_TEMPLATE["fields"][1],
            ]
        ))

        for i in range(len(fields)):
            for j in range(len(fields[i].cells)):
                for k in range(len(fields[i].cells[j])):
                    fields[i].cells[j][k] = Cell.from_hash(hashed_cells[i][j][k])

        self._fields = fields
