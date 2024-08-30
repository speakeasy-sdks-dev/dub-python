"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AnalyticsReferersTypedDict(TypedDict):
    referer: str
    r"""The name of the referer. If unknown, this will be `(direct)`"""
    clicks: NotRequired[float]
    r"""The number of clicks from this referer"""
    leads: NotRequired[float]
    r"""The number of leads from this referer"""
    sales: NotRequired[float]
    r"""The number of sales from this referer"""
    sale_amount: NotRequired[float]
    r"""The total amount of sales from this referer"""
    

class AnalyticsReferers(BaseModel):
    referer: str
    r"""The name of the referer. If unknown, this will be `(direct)`"""
    clicks: Optional[float] = 0
    r"""The number of clicks from this referer"""
    leads: Optional[float] = 0
    r"""The number of leads from this referer"""
    sales: Optional[float] = 0
    r"""The number of sales from this referer"""
    sale_amount: Annotated[Optional[float], pydantic.Field(alias="saleAmount")] = 0
    r"""The total amount of sales from this referer"""
    
