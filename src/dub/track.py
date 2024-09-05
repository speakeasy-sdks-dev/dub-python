"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from dub import utils
from dub._hooks import HookContext
from dub.models import errors, operations
from dub.types import BaseModel, OptionalNullable, SDKError, UNSET
from typing import Any, Optional, Union, cast

class Track(BaseSDK):
    
    
    def lead(
        self, *,
        request: Optional[Union[operations.TrackLeadRequestBody, operations.TrackLeadRequestBodyTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[operations.TrackLeadResponseBody]:
        r"""Track a lead

        Track a lead for a short link.

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
        
        if not isinstance(request, BaseModel) and request is not None:
            request = utils.unmarshal(request, operations.TrackLeadRequestBody)
        request = cast(operations.TrackLeadRequestBody, request)
        
        req = self.build_request(
            method="POST",
            path="/track/lead",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[operations.TrackLeadRequestBody]),
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
            hook_ctx=HookContext(operation_id="trackLead", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","409","410","422","429","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[operations.TrackLeadResponseBody])
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
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def lead_async(
        self, *,
        request: Optional[Union[operations.TrackLeadRequestBody, operations.TrackLeadRequestBodyTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[operations.TrackLeadResponseBody]:
        r"""Track a lead

        Track a lead for a short link.

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
        
        if not isinstance(request, BaseModel) and request is not None:
            request = utils.unmarshal(request, operations.TrackLeadRequestBody)
        request = cast(operations.TrackLeadRequestBody, request)
        
        req = self.build_request(
            method="POST",
            path="/track/lead",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[operations.TrackLeadRequestBody]),
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
            hook_ctx=HookContext(operation_id="trackLead", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","409","410","422","429","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[operations.TrackLeadResponseBody])
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
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def sale(
        self, *,
        request: Optional[Union[operations.TrackSaleRequestBody, operations.TrackSaleRequestBodyTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[operations.TrackSaleResponseBody]:
        r"""Track a sale

        Track a sale for a short link.

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
        
        if not isinstance(request, BaseModel) and request is not None:
            request = utils.unmarshal(request, operations.TrackSaleRequestBody)
        request = cast(operations.TrackSaleRequestBody, request)
        
        req = self.build_request(
            method="POST",
            path="/track/sale",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[operations.TrackSaleRequestBody]),
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
            hook_ctx=HookContext(operation_id="trackSale", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","409","410","422","429","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[operations.TrackSaleResponseBody])
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
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def sale_async(
        self, *,
        request: Optional[Union[operations.TrackSaleRequestBody, operations.TrackSaleRequestBodyTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[operations.TrackSaleResponseBody]:
        r"""Track a sale

        Track a sale for a short link.

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
        
        if not isinstance(request, BaseModel) and request is not None:
            request = utils.unmarshal(request, operations.TrackSaleRequestBody)
        request = cast(operations.TrackSaleRequestBody, request)
        
        req = self.build_request(
            method="POST",
            path="/track/sale",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[operations.TrackSaleRequestBody]),
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
            hook_ctx=HookContext(operation_id="trackSale", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","409","410","422","429","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[operations.TrackSaleResponseBody])
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
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def customer(
        self, *,
        request: Optional[Union[operations.TrackCustomerRequestBody, operations.TrackCustomerRequestBodyTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[operations.TrackCustomerResponseBody]:
        r"""Track a customer

        Track a customer for an authenticated workspace.

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
        
        if not isinstance(request, BaseModel) and request is not None:
            request = utils.unmarshal(request, operations.TrackCustomerRequestBody)
        request = cast(operations.TrackCustomerRequestBody, request)
        
        req = self.build_request(
            method="POST",
            path="/track/customer",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[operations.TrackCustomerRequestBody]),
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
            hook_ctx=HookContext(operation_id="trackCustomer", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","409","410","422","429","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[operations.TrackCustomerResponseBody])
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
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def customer_async(
        self, *,
        request: Optional[Union[operations.TrackCustomerRequestBody, operations.TrackCustomerRequestBodyTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[operations.TrackCustomerResponseBody]:
        r"""Track a customer

        Track a customer for an authenticated workspace.

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
        
        if not isinstance(request, BaseModel) and request is not None:
            request = utils.unmarshal(request, operations.TrackCustomerRequestBody)
        request = cast(operations.TrackCustomerRequestBody, request)
        
        req = self.build_request(
            method="POST",
            path="/track/customer",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[operations.TrackCustomerRequestBody]),
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
            hook_ctx=HookContext(operation_id="trackCustomer", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","409","410","422","429","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[operations.TrackCustomerResponseBody])
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
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
