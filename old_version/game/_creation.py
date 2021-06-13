from old_version.game.player.field import Field
from old_version.game.utils import FILE_TEMPLATE


def create_fields(self):
    for field in FILE_TEMPLATE["fields"]:
        [x, y] = field["position"]
        [width, height] = field["size"]

        field_object = Field(width, height, x, y)
        field_object.fill()

        self._fields.append(field_object)
