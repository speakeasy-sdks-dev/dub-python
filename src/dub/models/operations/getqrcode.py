"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from dub.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class Level(str, Enum):
    r"""The level of error correction to use for the QR code. Defaults to `L` if not provided."""
    L = "L"
    M = "M"
    Q = "Q"
    H = "H"

class GetQRCodeRequestTypedDict(TypedDict):
    url: str
    r"""The URL to generate a QR code for."""
    size: NotRequired[float]
    r"""The size of the QR code in pixels. Defaults to `600` if not provided."""
    level: NotRequired[Level]
    r"""The level of error correction to use for the QR code. Defaults to `L` if not provided."""
    fg_color: NotRequired[str]
    r"""The foreground color of the QR code in hex format. Defaults to `#000000` if not provided."""
    bg_color: NotRequired[str]
    r"""The background color of the QR code in hex format. Defaults to `#ffffff` if not provided."""
    include_margin: NotRequired[bool]
    r"""Whether to include a margin around the QR code. Defaults to `false` if not provided."""
    

class GetQRCodeRequest(BaseModel):
    url: Annotated[str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    r"""The URL to generate a QR code for."""
    size: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 600
    r"""The size of the QR code in pixels. Defaults to `600` if not provided."""
    level: Annotated[Optional[Level], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = Level.L
    r"""The level of error correction to use for the QR code. Defaults to `L` if not provided."""
    fg_color: Annotated[Optional[str], pydantic.Field(alias="fgColor"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = "#000000"
    r"""The foreground color of the QR code in hex format. Defaults to `#000000` if not provided."""
    bg_color: Annotated[Optional[str], pydantic.Field(alias="bgColor"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = "#FFFFFF"
    r"""The background color of the QR code in hex format. Defaults to `#ffffff` if not provided."""
    include_margin: Annotated[Optional[bool], pydantic.Field(alias="includeMargin"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = True
    r"""Whether to include a margin around the QR code. Defaults to `false` if not provided."""
    
