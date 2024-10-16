"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from dub.utils import FieldMetadata, SecurityMetadata
from typing import TypedDict
from typing_extensions import Annotated


class SecurityTypedDict(TypedDict):
    token: str
    

class Security(BaseModel):
    token: Annotated[str, FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))]
    
