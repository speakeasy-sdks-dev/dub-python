"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Trigger(str, Enum):
    r"""The type of trigger method: link click or QR scan"""

    QR = "qr"
    LINK = "link"


class AnalyticsTriggersTypedDict(TypedDict):
    trigger: Trigger
    r"""The type of trigger method: link click or QR scan"""
    clicks: NotRequired[float]
    r"""The number of clicks from this trigger method"""
    leads: NotRequired[float]
    r"""The number of leads from this trigger method"""
    sales: NotRequired[float]
    r"""The number of sales from this trigger method"""
    sale_amount: NotRequired[float]
    r"""The total amount of sales from this trigger method, in cents"""


class AnalyticsTriggers(BaseModel):
    trigger: Trigger
    r"""The type of trigger method: link click or QR scan"""

    clicks: Optional[float] = 0
    r"""The number of clicks from this trigger method"""

    leads: Optional[float] = 0
    r"""The number of leads from this trigger method"""

    sales: Optional[float] = 0
    r"""The number of sales from this trigger method"""

    sale_amount: Annotated[Optional[float], pydantic.Field(alias="saleAmount")] = 0
    r"""The total amount of sales from this trigger method, in cents"""
