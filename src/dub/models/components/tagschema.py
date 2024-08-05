"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from enum import Enum
from typing import TypedDict


class Color(str, Enum):
    r"""The color of the tag."""
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    PINK = "pink"
    BROWN = "brown"

class TagSchemaTypedDict(TypedDict):
    id: str
    r"""The unique ID of the tag."""
    name: str
    r"""The name of the tag."""
    color: Color
    r"""The color of the tag."""
    

class TagSchema(BaseModel):
    id: str
    r"""The unique ID of the tag."""
    name: str
    r"""The name of the tag."""
    color: Color
    r"""The color of the tag."""
    
