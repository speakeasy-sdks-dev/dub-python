"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, OptionalNullable, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class Plan(str, Enum):
    r"""The plan of the workspace."""

    FREE = "free"
    PRO = "pro"
    BUSINESS = "business"
    BUSINESS_PLUS = "business plus"
    BUSINESS_EXTRA = "business extra"
    BUSINESS_MAX = "business max"
    ENTERPRISE = "enterprise"


class Role(str, Enum):
    r"""The role of the authenticated user in the workspace."""

    OWNER = "owner"
    MEMBER = "member"


class UsersTypedDict(TypedDict):
    role: Role
    r"""The role of the authenticated user in the workspace."""


class Users(BaseModel):
    role: Role
    r"""The role of the authenticated user in the workspace."""


class DomainsTypedDict(TypedDict):
    slug: str
    r"""The domain name."""
    primary: NotRequired[bool]
    r"""Whether the domain is the primary domain for the workspace."""
    verified: NotRequired[bool]
    r"""Whether the domain is verified."""


class Domains(BaseModel):
    slug: str
    r"""The domain name."""

    primary: Optional[bool] = False
    r"""Whether the domain is the primary domain for the workspace."""

    verified: Optional[bool] = False
    r"""Whether the domain is verified."""


class WorkspaceSchemaTypedDict(TypedDict):
    id: str
    r"""The unique ID of the workspace."""
    name: str
    r"""The name of the workspace."""
    slug: str
    r"""The slug of the workspace."""
    plan: Plan
    r"""The plan of the workspace."""
    stripe_id: Nullable[str]
    r"""The Stripe ID of the workspace."""
    billing_cycle_start: float
    r"""The date and time when the billing cycle starts for the workspace."""
    stripe_connect_id: Nullable[str]
    r"""[BETA]: The Stripe Connect ID of the workspace."""
    invite_code: Nullable[str]
    r"""The invite code of the workspace."""
    usage: float
    r"""The usage of the workspace."""
    usage_limit: float
    r"""The usage limit of the workspace."""
    links_usage: float
    r"""The links usage of the workspace."""
    links_limit: float
    r"""The links limit of the workspace."""
    sales_usage: float
    r"""The dollar amount of tracked revenue in the current billing cycle (in cents)."""
    sales_limit: float
    r"""The limit of tracked revenue in the current billing cycle (in cents)."""
    domains_limit: float
    r"""The domains limit of the workspace."""
    tags_limit: float
    r"""The tags limit of the workspace."""
    users_limit: float
    r"""The users limit of the workspace."""
    ai_usage: float
    r"""The AI usage of the workspace."""
    ai_limit: float
    r"""The AI limit of the workspace."""
    referral_link_id: Nullable[str]
    r"""The ID of the referral link of the workspace."""
    conversion_enabled: bool
    r"""Whether the workspace has conversion tracking enabled (d.to/conversions)."""
    dot_link_claimed: bool
    r"""Whether the workspace has claimed a free .link domain. (dub.link/free)"""
    created_at: str
    r"""The date and time when the workspace was created."""
    users: List[UsersTypedDict]
    r"""The role of the authenticated user in the workspace."""
    domains: List[DomainsTypedDict]
    r"""The domains of the workspace."""
    logo: NotRequired[Nullable[str]]
    r"""The logo of the workspace."""
    flags: NotRequired[Dict[str, bool]]
    r"""The feature flags of the workspace, indicating which features are enabled."""


class WorkspaceSchema(BaseModel):
    id: str
    r"""The unique ID of the workspace."""

    name: str
    r"""The name of the workspace."""

    slug: str
    r"""The slug of the workspace."""

    plan: Plan
    r"""The plan of the workspace."""

    stripe_id: Annotated[Nullable[str], pydantic.Field(alias="stripeId")]
    r"""The Stripe ID of the workspace."""

    billing_cycle_start: Annotated[float, pydantic.Field(alias="billingCycleStart")]
    r"""The date and time when the billing cycle starts for the workspace."""

    stripe_connect_id: Annotated[Nullable[str], pydantic.Field(alias="stripeConnectId")]
    r"""[BETA]: The Stripe Connect ID of the workspace."""

    invite_code: Annotated[Nullable[str], pydantic.Field(alias="inviteCode")]
    r"""The invite code of the workspace."""

    usage: float
    r"""The usage of the workspace."""

    usage_limit: Annotated[float, pydantic.Field(alias="usageLimit")]
    r"""The usage limit of the workspace."""

    links_usage: Annotated[float, pydantic.Field(alias="linksUsage")]
    r"""The links usage of the workspace."""

    links_limit: Annotated[float, pydantic.Field(alias="linksLimit")]
    r"""The links limit of the workspace."""

    sales_usage: Annotated[float, pydantic.Field(alias="salesUsage")]
    r"""The dollar amount of tracked revenue in the current billing cycle (in cents)."""

    sales_limit: Annotated[float, pydantic.Field(alias="salesLimit")]
    r"""The limit of tracked revenue in the current billing cycle (in cents)."""

    domains_limit: Annotated[float, pydantic.Field(alias="domainsLimit")]
    r"""The domains limit of the workspace."""

    tags_limit: Annotated[float, pydantic.Field(alias="tagsLimit")]
    r"""The tags limit of the workspace."""

    users_limit: Annotated[float, pydantic.Field(alias="usersLimit")]
    r"""The users limit of the workspace."""

    ai_usage: Annotated[float, pydantic.Field(alias="aiUsage")]
    r"""The AI usage of the workspace."""

    ai_limit: Annotated[float, pydantic.Field(alias="aiLimit")]
    r"""The AI limit of the workspace."""

    referral_link_id: Annotated[Nullable[str], pydantic.Field(alias="referralLinkId")]
    r"""The ID of the referral link of the workspace."""

    conversion_enabled: Annotated[bool, pydantic.Field(alias="conversionEnabled")]
    r"""Whether the workspace has conversion tracking enabled (d.to/conversions)."""

    dot_link_claimed: Annotated[bool, pydantic.Field(alias="dotLinkClaimed")]
    r"""Whether the workspace has claimed a free .link domain. (dub.link/free)"""

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]
    r"""The date and time when the workspace was created."""

    users: List[Users]
    r"""The role of the authenticated user in the workspace."""

    domains: List[Domains]
    r"""The domains of the workspace."""

    logo: OptionalNullable[str] = None
    r"""The logo of the workspace."""

    flags: Optional[Dict[str, bool]] = None
    r"""The feature flags of the workspace, indicating which features are enabled."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["logo", "flags"]
        nullable_fields = [
            "stripeId",
            "stripeConnectId",
            "inviteCode",
            "referralLinkId",
            "logo",
        ]
        null_default_fields = ["logo"]

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
