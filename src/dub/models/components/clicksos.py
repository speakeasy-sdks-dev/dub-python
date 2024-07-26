"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class ClicksOSTypedDict(TypedDict):
    os: str
    r"""The name of the OS"""
    clicks: float
    r"""The number of clicks from this OS"""
    

class ClicksOS(BaseModel):
    os: str
    r"""The name of the OS"""
    clicks: float
    r"""The number of clicks from this OS"""
    
