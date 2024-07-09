"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TrackCustomerRequestBodyTypedDict(TypedDict):
    customer_id: str
    r"""This is the unique identifier for the customer in the client's app. This is used to track the customer's journey."""
    customer_name: NotRequired[str]
    r"""Name of the customer in the client's app."""
    customer_email: NotRequired[str]
    r"""Email of the customer in the client's app."""
    customer_avatar: NotRequired[str]
    r"""Avatar of the customer in the client's app."""
    

class TrackCustomerRequestBody(BaseModel):
    customer_id: Annotated[str, pydantic.Field(alias="customerId")]
    r"""This is the unique identifier for the customer in the client's app. This is used to track the customer's journey."""
    customer_name: Annotated[Optional[str], pydantic.Field(alias="customerName")] = None
    r"""Name of the customer in the client's app."""
    customer_email: Annotated[Optional[str], pydantic.Field(alias="customerEmail")] = None
    r"""Email of the customer in the client's app."""
    customer_avatar: Annotated[Optional[str], pydantic.Field(alias="customerAvatar")] = None
    r"""Avatar of the customer in the client's app."""
    

class TrackCustomerResponseBodyTypedDict(TypedDict):
    r"""A customer was tracked."""
    
    customer_id: str
    customer_name: Nullable[str]
    customer_email: Nullable[str]
    customer_avatar: Nullable[str]
    

class TrackCustomerResponseBody(BaseModel):
    r"""A customer was tracked."""
    
    customer_id: Annotated[str, pydantic.Field(alias="customerId")]
    customer_name: Annotated[Nullable[str], pydantic.Field(alias="customerName")]
    customer_email: Annotated[Nullable[str], pydantic.Field(alias="customerEmail")]
    customer_avatar: Annotated[Nullable[str], pydantic.Field(alias="customerAvatar")]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
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
        
