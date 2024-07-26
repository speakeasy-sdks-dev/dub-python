"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from dub.utils import FieldMetadata, SecurityMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SecurityTypedDict(TypedDict):
    token: NotRequired[str]
    

class Security(BaseModel):
    token: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    
