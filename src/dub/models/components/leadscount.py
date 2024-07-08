"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class LeadsCountTypedDict(TypedDict):
    leads: float
    r"""The total number of leads"""
    

class LeadsCount(BaseModel):
    leads: float
    r"""The total number of leads"""
    
