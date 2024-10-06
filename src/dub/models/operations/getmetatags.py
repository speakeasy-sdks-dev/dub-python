"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, UNSET_SENTINEL
from dub.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing_extensions import Annotated, TypedDict


class GetMetatagsRequestTypedDict(TypedDict):
    url: str
    r"""The URL to retrieve metatags for."""


class GetMetatagsRequest(BaseModel):
    url: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The URL to retrieve metatags for."""


class GetMetatagsResponseBodyTypedDict(TypedDict):
    r"""The retrieved metatags"""

    title: Nullable[str]
    r"""The meta title tag for the URL."""
    description: Nullable[str]
    r"""The meta description tag for the URL."""
    image: Nullable[str]
    r"""The OpenGraph image for the URL."""


class GetMetatagsResponseBody(BaseModel):
    r"""The retrieved metatags"""

    title: Nullable[str]
    r"""The meta title tag for the URL."""

    description: Nullable[str]
    r"""The meta description tag for the URL."""

    image: Nullable[str]
    r"""The OpenGraph image for the URL."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["title", "description", "image"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
