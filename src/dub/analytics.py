"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from dub._hooks import HookContext
from dub.models import errors, operations
from dub.types import BaseModel, OptionalNullable, UNSET
import dub.utils as utils
from typing import Optional, Union

class Analytics(BaseSDK):
    
    
    def retrieve(
        self, *,
        request: Optional[Union[operations.RetrieveAnalyticsRequest, operations.RetrieveAnalyticsRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.RetrieveAnalyticsResponseBody:
        r"""Retrieve analytics for a link, a domain, or the authenticated workspace.

        Retrieve analytics for a link, a domain, or the authenticated workspace. The response type depends on the `event` and `type` query parameters.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.RetrieveAnalyticsRequest)
        
        req = self.build_request(
            method="GET",
            path="/analytics",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="retrieveAnalytics", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","409","410","422","429","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[operations.RetrieveAnalyticsResponseBody])
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.BadRequestData)
            raise errors.BadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.UnauthorizedData)
            raise errors.Unauthorized(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ForbiddenData)
            raise errors.Forbidden(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.NotFoundData)
            raise errors.NotFound(data=data)
        if utils.match_response(http_res, "409", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ConflictData)
            raise errors.Conflict(data=data)
        if utils.match_response(http_res, "410", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.InviteExpiredData)
            raise errors.InviteExpired(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.UnprocessableEntityData)
            raise errors.UnprocessableEntity(data=data)
        if utils.match_response(http_res, "429", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.RateLimitExceededData)
            raise errors.RateLimitExceeded(data=data)
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.InternalServerErrorData)
            raise errors.InternalServerError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def retrieve_async(
        self, *,
        request: Optional[Union[operations.RetrieveAnalyticsRequest, operations.RetrieveAnalyticsRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.RetrieveAnalyticsResponseBody:
        r"""Retrieve analytics for a link, a domain, or the authenticated workspace.

        Retrieve analytics for a link, a domain, or the authenticated workspace. The response type depends on the `event` and `type` query parameters.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.RetrieveAnalyticsRequest)
        
        req = self.build_request(
            method="GET",
            path="/analytics",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="retrieveAnalytics", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","409","410","422","429","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[operations.RetrieveAnalyticsResponseBody])
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.BadRequestData)
            raise errors.BadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.UnauthorizedData)
            raise errors.Unauthorized(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ForbiddenData)
            raise errors.Forbidden(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.NotFoundData)
            raise errors.NotFound(data=data)
        if utils.match_response(http_res, "409", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ConflictData)
            raise errors.Conflict(data=data)
        if utils.match_response(http_res, "410", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.InviteExpiredData)
            raise errors.InviteExpired(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.UnprocessableEntityData)
            raise errors.UnprocessableEntity(data=data)
        if utils.match_response(http_res, "429", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.RateLimitExceededData)
            raise errors.RateLimitExceeded(data=data)
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.InternalServerErrorData)
            raise errors.InternalServerError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
