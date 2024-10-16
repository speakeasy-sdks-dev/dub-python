"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class SalesCountTypedDict(TypedDict):
    sales: float
    r"""The total number of sales"""
    amount: float
    r"""The total amount of sales"""
    

class SalesCount(BaseModel):
    sales: float
    r"""The total number of sales"""
    amount: float
    r"""The total amount of sales"""
    
