"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class ClicksDevicesTypedDict(TypedDict):
    device: str
    r"""The name of the device"""
    clicks: float
    r"""The number of clicks from this device"""
    

class ClicksDevices(BaseModel):
    device: str
    r"""The name of the device"""
    clicks: float
    r"""The number of clicks from this device"""
    
