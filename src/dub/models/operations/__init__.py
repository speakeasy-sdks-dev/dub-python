"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .bulkcreatelinks import BulkCreateLinksTagIds, BulkCreateLinksTagIdsTypedDict, BulkCreateLinksTagNames, BulkCreateLinksTagNamesTypedDict, RequestBody, RequestBodyTypedDict
from .bulkupdatelinks import BulkUpdateLinksRequestBody, BulkUpdateLinksRequestBodyTypedDict, BulkUpdateLinksTagIds, BulkUpdateLinksTagIdsTypedDict, BulkUpdateLinksTagNames, BulkUpdateLinksTagNamesTypedDict, Data, DataTypedDict
from .createdomain import CreateDomainRequestBody, CreateDomainRequestBodyTypedDict
from .createlink import CreateLinkRequestBody, CreateLinkRequestBodyTypedDict, TagIds, TagIdsTypedDict, TagNames, TagNamesTypedDict
from .createtag import Color, CreateTagRequestBody, CreateTagRequestBodyTypedDict
from .deletedomain import DeleteDomainRequest, DeleteDomainRequestTypedDict, DeleteDomainResponseBody, DeleteDomainResponseBodyTypedDict
from .deletelink import DeleteLinkRequest, DeleteLinkRequestTypedDict, DeleteLinkResponseBody, DeleteLinkResponseBodyTypedDict
from .getlinkinfo import GetLinkInfoRequest, GetLinkInfoRequestTypedDict
from .getlinks import GetLinksRequest, GetLinksRequestTypedDict, GetLinksResponse, GetLinksResponseTypedDict, QueryParamTagIds, QueryParamTagIdsTypedDict, QueryParamTagNames, QueryParamTagNamesTypedDict, Sort
from .getlinkscount import GetLinksCountQueryParamTagIds, GetLinksCountQueryParamTagIdsTypedDict, GetLinksCountQueryParamTagNames, GetLinksCountQueryParamTagNamesTypedDict, GetLinksCountRequest, GetLinksCountRequestTypedDict, GroupBy, GroupByTypedDict, One, Three, Two
from .getmetatags import GetMetatagsRequest, GetMetatagsRequestTypedDict, GetMetatagsResponseBody, GetMetatagsResponseBodyTypedDict
from .getqrcode import GetQRCodeRequest, GetQRCodeRequestTypedDict, Level
from .getworkspace import GetWorkspaceRequest, GetWorkspaceRequestTypedDict
from .listdomains import ListDomainsRequest, ListDomainsRequestTypedDict, ListDomainsResponse, ListDomainsResponseTypedDict
from .listevents import ListEventsRequest, ListEventsRequestTypedDict, Order, QueryParamEvent, QueryParamInterval, SortBy
from .retrieveanalytics import Event, Interval, QueryParamGroupBy, RetrieveAnalyticsRequest, RetrieveAnalyticsRequestTypedDict, RetrieveAnalyticsResponseBody, RetrieveAnalyticsResponseBodyTypedDict
from .trackcustomer import TrackCustomerRequestBody, TrackCustomerRequestBodyTypedDict, TrackCustomerResponseBody, TrackCustomerResponseBodyTypedDict
from .tracklead import TrackLeadRequestBody, TrackLeadRequestBodyTypedDict, TrackLeadResponseBody, TrackLeadResponseBodyTypedDict
from .tracksale import PaymentProcessor, TrackSaleRequestBody, TrackSaleRequestBodyTypedDict, TrackSaleResponseBody, TrackSaleResponseBodyTypedDict
from .updatedomain import UpdateDomainRequest, UpdateDomainRequestBody, UpdateDomainRequestBodyTypedDict, UpdateDomainRequestTypedDict
from .updatelink import UpdateLinkRequest, UpdateLinkRequestBody, UpdateLinkRequestBodyTypedDict, UpdateLinkRequestTypedDict, UpdateLinkTagIds, UpdateLinkTagIdsTypedDict, UpdateLinkTagNames, UpdateLinkTagNamesTypedDict
from .updatetag import UpdateTagColor, UpdateTagRequest, UpdateTagRequestBody, UpdateTagRequestBodyTypedDict, UpdateTagRequestTypedDict
from .updateworkspace import UpdateWorkspaceRequest, UpdateWorkspaceRequestBody, UpdateWorkspaceRequestBodyTypedDict, UpdateWorkspaceRequestTypedDict
from .upsertlink import UpsertLinkRequestBody, UpsertLinkRequestBodyTypedDict, UpsertLinkTagIds, UpsertLinkTagIdsTypedDict, UpsertLinkTagNames, UpsertLinkTagNamesTypedDict

__all__ = ["BulkCreateLinksTagIds", "BulkCreateLinksTagIdsTypedDict", "BulkCreateLinksTagNames", "BulkCreateLinksTagNamesTypedDict", "BulkUpdateLinksRequestBody", "BulkUpdateLinksRequestBodyTypedDict", "BulkUpdateLinksTagIds", "BulkUpdateLinksTagIdsTypedDict", "BulkUpdateLinksTagNames", "BulkUpdateLinksTagNamesTypedDict", "Color", "CreateDomainRequestBody", "CreateDomainRequestBodyTypedDict", "CreateLinkRequestBody", "CreateLinkRequestBodyTypedDict", "CreateTagRequestBody", "CreateTagRequestBodyTypedDict", "Data", "DataTypedDict", "DeleteDomainRequest", "DeleteDomainRequestTypedDict", "DeleteDomainResponseBody", "DeleteDomainResponseBodyTypedDict", "DeleteLinkRequest", "DeleteLinkRequestTypedDict", "DeleteLinkResponseBody", "DeleteLinkResponseBodyTypedDict", "Event", "GetLinkInfoRequest", "GetLinkInfoRequestTypedDict", "GetLinksCountQueryParamTagIds", "GetLinksCountQueryParamTagIdsTypedDict", "GetLinksCountQueryParamTagNames", "GetLinksCountQueryParamTagNamesTypedDict", "GetLinksCountRequest", "GetLinksCountRequestTypedDict", "GetLinksRequest", "GetLinksRequestTypedDict", "GetLinksResponse", "GetLinksResponseTypedDict", "GetMetatagsRequest", "GetMetatagsRequestTypedDict", "GetMetatagsResponseBody", "GetMetatagsResponseBodyTypedDict", "GetQRCodeRequest", "GetQRCodeRequestTypedDict", "GetWorkspaceRequest", "GetWorkspaceRequestTypedDict", "GroupBy", "GroupByTypedDict", "Interval", "Level", "ListDomainsRequest", "ListDomainsRequestTypedDict", "ListDomainsResponse", "ListDomainsResponseTypedDict", "ListEventsRequest", "ListEventsRequestTypedDict", "One", "Order", "PaymentProcessor", "QueryParamEvent", "QueryParamGroupBy", "QueryParamInterval", "QueryParamTagIds", "QueryParamTagIdsTypedDict", "QueryParamTagNames", "QueryParamTagNamesTypedDict", "RequestBody", "RequestBodyTypedDict", "RetrieveAnalyticsRequest", "RetrieveAnalyticsRequestTypedDict", "RetrieveAnalyticsResponseBody", "RetrieveAnalyticsResponseBodyTypedDict", "Sort", "SortBy", "TagIds", "TagIdsTypedDict", "TagNames", "TagNamesTypedDict", "Three", "TrackCustomerRequestBody", "TrackCustomerRequestBodyTypedDict", "TrackCustomerResponseBody", "TrackCustomerResponseBodyTypedDict", "TrackLeadRequestBody", "TrackLeadRequestBodyTypedDict", "TrackLeadResponseBody", "TrackLeadResponseBodyTypedDict", "TrackSaleRequestBody", "TrackSaleRequestBodyTypedDict", "TrackSaleResponseBody", "TrackSaleResponseBodyTypedDict", "Two", "UpdateDomainRequest", "UpdateDomainRequestBody", "UpdateDomainRequestBodyTypedDict", "UpdateDomainRequestTypedDict", "UpdateLinkRequest", "UpdateLinkRequestBody", "UpdateLinkRequestBodyTypedDict", "UpdateLinkRequestTypedDict", "UpdateLinkTagIds", "UpdateLinkTagIdsTypedDict", "UpdateLinkTagNames", "UpdateLinkTagNamesTypedDict", "UpdateTagColor", "UpdateTagRequest", "UpdateTagRequestBody", "UpdateTagRequestBodyTypedDict", "UpdateTagRequestTypedDict", "UpdateWorkspaceRequest", "UpdateWorkspaceRequestBody", "UpdateWorkspaceRequestBodyTypedDict", "UpdateWorkspaceRequestTypedDict", "UpsertLinkRequestBody", "UpsertLinkRequestBodyTypedDict", "UpsertLinkTagIds", "UpsertLinkTagIdsTypedDict", "UpsertLinkTagNames", "UpsertLinkTagNamesTypedDict"]
