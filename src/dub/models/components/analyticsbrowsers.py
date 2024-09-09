"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AnalyticsBrowsersTypedDict(TypedDict):
    browser: str
    r"""The name of the browser"""
    clicks: NotRequired[float]
    r"""The number of clicks from this browser"""
    leads: NotRequired[float]
    r"""The number of leads from this browser"""
    sales: NotRequired[float]
    r"""The number of sales from this browser"""
    sale_amount: NotRequired[float]
    r"""The total amount of sales from this browser"""


class AnalyticsBrowsers(BaseModel):
    browser: str
    r"""The name of the browser"""

    clicks: Optional[float] = 0
    r"""The number of clicks from this browser"""

    leads: Optional[float] = 0
    r"""The number of leads from this browser"""

    sales: Optional[float] = 0
    r"""The number of sales from this browser"""

    sale_amount: Annotated[Optional[float], pydantic.Field(alias="saleAmount")] = 0
    r"""The total amount of sales from this browser"""
