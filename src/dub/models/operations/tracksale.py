"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PaymentProcessor(str, Enum):
    r"""The payment processor via which the sale was made."""
    STRIPE = "stripe"
    SHOPIFY = "shopify"
    PADDLE = "paddle"

class TrackSaleRequestBodyTypedDict(TypedDict):
    customer_id: str
    r"""This is the unique identifier for the customer in the client's app. This is used to track the customer's journey."""
    amount: int
    r"""The amount of the sale. Should be passed in cents."""
    payment_processor: PaymentProcessor
    r"""The payment processor via which the sale was made."""
    event_name: NotRequired[str]
    r"""The name of the sale event. It can be used to track different types of event for example 'Purchase', 'Upgrade', 'Payment', etc."""
    invoice_id: NotRequired[Nullable[str]]
    r"""The invoice ID of the sale."""
    currency: NotRequired[str]
    r"""The currency of the sale. Accepts ISO 4217 currency codes."""
    metadata: NotRequired[Nullable[Dict[str, Any]]]
    r"""Additional metadata to be stored with the sale event."""
    

class TrackSaleRequestBody(BaseModel):
    customer_id: Annotated[str, pydantic.Field(alias="customerId")]
    r"""This is the unique identifier for the customer in the client's app. This is used to track the customer's journey."""
    amount: int
    r"""The amount of the sale. Should be passed in cents."""
    payment_processor: Annotated[PaymentProcessor, pydantic.Field(alias="paymentProcessor")]
    r"""The payment processor via which the sale was made."""
    event_name: Annotated[Optional[str], pydantic.Field(alias="eventName")] = "Purchase"
    r"""The name of the sale event. It can be used to track different types of event for example 'Purchase', 'Upgrade', 'Payment', etc."""
    invoice_id: Annotated[OptionalNullable[str], pydantic.Field(alias="invoiceId")] = None
    r"""The invoice ID of the sale."""
    currency: Optional[str] = "usd"
    r"""The currency of the sale. Accepts ISO 4217 currency codes."""
    metadata: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Additional metadata to be stored with the sale event."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["eventName", "invoiceId", "currency", "metadata"]
        nullable_fields = ["invoiceId", "metadata"]
        null_default_fields = ["invoiceId"]

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        

class TrackSaleResponseBodyTypedDict(TypedDict):
    r"""A sale was tracked."""
    
    event_name: str
    customer_id: str
    amount: float
    payment_processor: str
    invoice_id: Nullable[str]
    currency: str
    metadata: Nullable[Dict[str, Any]]
    

class TrackSaleResponseBody(BaseModel):
    r"""A sale was tracked."""
    
    event_name: Annotated[str, pydantic.Field(alias="eventName")]
    customer_id: Annotated[str, pydantic.Field(alias="customerId")]
    amount: float
    payment_processor: Annotated[str, pydantic.Field(alias="paymentProcessor")]
    invoice_id: Annotated[Nullable[str], pydantic.Field(alias="invoiceId")]
    currency: str
    metadata: Nullable[Dict[str, Any]]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["invoiceId", "metadata"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        
