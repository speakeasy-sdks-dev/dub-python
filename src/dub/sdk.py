"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.retries import RetryConfig
from dub._hooks import SDKHooks
from dub.analytics import Analytics
from dub.domains import Domains
from dub.links import Links
from dub.metatags import Metatags
from dub.models import components
from dub.qr_codes import QRCodes
from dub.tags import Tags
from dub.track import Track
from dub.types import OptionalNullable, UNSET
import dub.utils as utils
from dub.workspaces import Workspaces
import httpx
from typing import Any, Callable, Dict, Optional, Union

class Dub(BaseSDK):
    r"""Dub.co API: Dub is link management infrastructure for companies to create marketing campaigns, link sharing features, and referral programs."""
    links: Links
    qr_codes: QRCodes
    analytics: Analytics
    workspaces: Workspaces
    tags: Tags
    domains: Domains
    track: Track
    metatags: Metatags
    def __init__(
        self,
        token: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param token: The token required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."
        
        security: Any = None
        if callable(token):
            security = lambda: components.Security(token = token()) # pylint: disable=unnecessary-lambda-assignment
        else:
            security = components.Security(token = token)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        BaseSDK.__init__(self, SDKConfiguration(
            client=client,
            async_client=async_client,
            security=security,
            server_url=server_url,
            server_idx=server_idx,
            retry_config=retry_config,
            timeout_ms=timeout_ms
        ))

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.links = Links(self.sdk_configuration)
        self.qr_codes = QRCodes(self.sdk_configuration)
        self.analytics = Analytics(self.sdk_configuration)
        self.workspaces = Workspaces(self.sdk_configuration)
        self.tags = Tags(self.sdk_configuration)
        self.domains = Domains(self.sdk_configuration)
        self.track = Track(self.sdk_configuration)
        self.metatags = Metatags(self.sdk_configuration)
    
