"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable
from dub.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateDomainGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]
    

class CreateDomainGlobals(BaseModel):
    workspace_id: Annotated[Optional[str], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.", alias="workspaceId"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    

class CreateDomainRequestBodyTypedDict(TypedDict):
    slug: str
    r"""Name of the domain."""
    expired_url: NotRequired[Nullable[str]]
    r"""Redirect users to a specific URL when any link under this domain has expired."""
    archived: NotRequired[bool]
    r"""Whether to archive this domain. `false` will unarchive a previously archived domain."""
    placeholder: NotRequired[Nullable[str]]
    r"""Provide context to your teammates in the link creation modal by showing them an example of a link to be shortened."""
    

class CreateDomainRequestBody(BaseModel):
    slug: str
    r"""Name of the domain."""
    expired_url: Annotated[Optional[Nullable[str]], pydantic.Field(alias="expiredUrl")] = None
    r"""Redirect users to a specific URL when any link under this domain has expired."""
    archived: Optional[bool] = False
    r"""Whether to archive this domain. `false` will unarchive a previously archived domain."""
    placeholder: Optional[Nullable[str]] = "https://dub.co/help/article/what-is-dub"
    r"""Provide context to your teammates in the link creation modal by showing them an example of a link to be shortened."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expiredUrl", "archived", "placeholder"]
        nullable_fields = ["expiredUrl", "placeholder"]
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
        
