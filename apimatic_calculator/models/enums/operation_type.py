from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OperationType(str, Enum):
    """Possible operators are sum, subtract, multiply, divide"""

    SUM = "SUM"
    SUBTRACT = "SUBTRACT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"

    __str__ = str.__str__


OperationTypeOrStr: TypeAlias = Annotated[OperationType | str, open_enum_validator(OperationType)]
