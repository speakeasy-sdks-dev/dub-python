"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class SalesDevicesTypedDict(TypedDict):
    device: str
    r"""The name of the device"""
    sales: float
    r"""The number of sales from this device"""
    amount: float
    r"""The total amount of sales from this device"""


class SalesDevices(BaseModel):
    device: str
    r"""The name of the device"""

    sales: float
    r"""The number of sales from this device"""

    amount: float
    r"""The total amount of sales from this device"""
