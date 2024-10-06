"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .leadcreatedevent import LeadCreatedEvent, LeadCreatedEventTypedDict
from .linkclickedevent import LinkClickedEvent, LinkClickedEventTypedDict
from .linkwebhookevent import LinkWebhookEvent, LinkWebhookEventTypedDict
from .salecreatedevent import SaleCreatedEvent, SaleCreatedEventTypedDict
from typing import Union


WebhookEventTypedDict = Union[
    LinkWebhookEventTypedDict,
    LinkClickedEventTypedDict,
    LeadCreatedEventTypedDict,
    SaleCreatedEventTypedDict,
]
r"""Webhook event schema"""


WebhookEvent = Union[
    LinkWebhookEvent, LinkClickedEvent, LeadCreatedEvent, SaleCreatedEvent
]
r"""Webhook event schema"""
