"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class ClicksTopUrlsTypedDict(TypedDict):
    url: str
    r"""The destination URL"""
    clicks: float
    r"""The number of clicks from this URL"""
    

class ClicksTopUrls(BaseModel):
    url: str
    r"""The destination URL"""
    clicks: float
    r"""The number of clicks from this URL"""
    
