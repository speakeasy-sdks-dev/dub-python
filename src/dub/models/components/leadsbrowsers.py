"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class LeadsBrowsersTypedDict(TypedDict):
    browser: str
    r"""The name of the browser"""
    leads: float
    r"""The number of leads from this browser"""
    

class LeadsBrowsers(BaseModel):
    browser: str
    r"""The name of the browser"""
    leads: float
    r"""The number of leads from this browser"""
    
