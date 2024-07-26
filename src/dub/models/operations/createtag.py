"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from enum import Enum
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class Color(str, Enum):
    r"""The color of the tag. If not provided, a random color will be used from the list: red, yellow, green, blue, purple, pink, brown."""
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    PINK = "pink"
    BROWN = "brown"

class CreateTagRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The name of the tag to create."""
    color: NotRequired[Color]
    r"""The color of the tag. If not provided, a random color will be used from the list: red, yellow, green, blue, purple, pink, brown."""
    tag: NotRequired[str]
    r"""The name of the tag to create."""
    

class CreateTagRequestBody(BaseModel):
    name: Optional[str] = None
    r"""The name of the tag to create."""
    color: Optional[Color] = None
    r"""The color of the tag. If not provided, a random color will be used from the list: red, yellow, green, blue, purple, pink, brown."""
    tag: Annotated[Optional[str], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.")] = None
    r"""The name of the tag to create."""
    
