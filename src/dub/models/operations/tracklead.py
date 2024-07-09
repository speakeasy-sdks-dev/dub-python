"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TrackLeadRequestBodyTypedDict(TypedDict):
    click_id: str
    r"""The ID of the click in th Dub. You can read this value from `dclid` cookie."""
    event_name: str
    r"""The name of the event to track."""
    customer_id: str
    r"""This is the unique identifier for the customer in the client's app. This is used to track the customer's journey."""
    customer_name: NotRequired[Nullable[str]]
    r"""Name of the customer in the client's app."""
    customer_email: NotRequired[Nullable[str]]
    r"""Email of the customer in the client's app."""
    customer_avatar: NotRequired[Nullable[str]]
    r"""Avatar of the customer in the client's app."""
    metadata: NotRequired[Nullable[Dict[str, Any]]]
    r"""Additional metadata to be stored with the lead event"""
    

class TrackLeadRequestBody(BaseModel):
    click_id: Annotated[str, pydantic.Field(alias="clickId")]
    r"""The ID of the click in th Dub. You can read this value from `dclid` cookie."""
    event_name: Annotated[str, pydantic.Field(alias="eventName")]
    r"""The name of the event to track."""
    customer_id: Annotated[str, pydantic.Field(alias="customerId")]
    r"""This is the unique identifier for the customer in the client's app. This is used to track the customer's journey."""
    customer_name: Annotated[Optional[Nullable[str]], pydantic.Field(alias="customerName")] = None
    r"""Name of the customer in the client's app."""
    customer_email: Annotated[Optional[Nullable[str]], pydantic.Field(alias="customerEmail")] = None
    r"""Email of the customer in the client's app."""
    customer_avatar: Annotated[Optional[Nullable[str]], pydantic.Field(alias="customerAvatar")] = None
    r"""Avatar of the customer in the client's app."""
    metadata: Optional[Nullable[Dict[str, Any]]] = None
    r"""Additional metadata to be stored with the lead event"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["customerName", "customerEmail", "customerAvatar", "metadata"]
        nullable_fields = ["customerName", "customerEmail", "customerAvatar", "metadata"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        

class TrackLeadResponseBodyTypedDict(TypedDict):
    r"""A lead was tracked."""
    
    click_id: str
    event_name: str
    customer_id: str
    customer_name: Nullable[str]
    customer_email: Nullable[str]
    customer_avatar: Nullable[str]
    metadata: NotRequired[Dict[str, Any]]
    

class TrackLeadResponseBody(BaseModel):
    r"""A lead was tracked."""
    
    click_id: Annotated[str, pydantic.Field(alias="clickId")]
    event_name: Annotated[str, pydantic.Field(alias="eventName")]
    customer_id: Annotated[str, pydantic.Field(alias="customerId")]
    customer_name: Annotated[Nullable[str], pydantic.Field(alias="customerName")]
    customer_email: Annotated[Nullable[str], pydantic.Field(alias="customerEmail")]
    customer_avatar: Annotated[Nullable[str], pydantic.Field(alias="customerAvatar")]
    metadata: Optional[Dict[str, Any]] = None
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata"]
        nullable_fields = ["customerName", "customerEmail", "customerAvatar"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        
