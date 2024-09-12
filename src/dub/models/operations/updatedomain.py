"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from dub.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateDomainRequestBodyTypedDict(TypedDict):
    slug: NotRequired[str]
    r"""Name of the domain."""
    expired_url: NotRequired[Nullable[str]]
    r"""Redirect users to a specific URL when any link under this domain has expired."""
    archived: NotRequired[bool]
    r"""Whether to archive this domain. `false` will unarchive a previously archived domain."""
    placeholder: NotRequired[Nullable[str]]
    r"""Provide context to your teammates in the link creation modal by showing them an example of a link to be shortened."""


class UpdateDomainRequestBody(BaseModel):
    slug: Optional[str] = None
    r"""Name of the domain."""

    expired_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="expiredUrl")
    ] = UNSET
    r"""Redirect users to a specific URL when any link under this domain has expired."""

    archived: Optional[bool] = False
    r"""Whether to archive this domain. `false` will unarchive a previously archived domain."""

    placeholder: OptionalNullable[str] = "https://dub.co/help/article/what-is-dub"
    r"""Provide context to your teammates in the link creation modal by showing them an example of a link to be shortened."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["slug", "expiredUrl", "archived", "placeholder"]
        nullable_fields = ["expiredUrl", "placeholder"]
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


class UpdateDomainRequestTypedDict(TypedDict):
    slug: str
    r"""The domain name."""
    request_body: NotRequired[UpdateDomainRequestBodyTypedDict]


class UpdateDomainRequest(BaseModel):
    slug: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The domain name."""

    request_body: Annotated[
        Optional[UpdateDomainRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
