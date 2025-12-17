# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import print_mail, address_verification, intl_address_verification
    from .resources.address_verification import AddressVerificationResource, AsyncAddressVerificationResource
    from .resources.print_mail.print_mail import PrintMailResource, AsyncPrintMailResource
    from .resources.intl_address_verification import (
        IntlAddressVerificationResource,
        AsyncIntlAddressVerificationResource,
    )

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "PostGrid",
    "AsyncPostGrid",
    "Client",
    "AsyncClient",
]


class PostGrid(SyncAPIClient):
    # client options
    address_verification_api_key: str | None
    print_mail_api_key: str | None

    def __init__(
        self,
        *,
        address_verification_api_key: str | None = None,
        print_mail_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous PostGrid client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `address_verification_api_key` from `POSTGRID_ADDRESS_VERIFICATION_API_KEY`
        - `print_mail_api_key` from `POSTGRID_PRINT_MAIL_API_KEY`
        """
        if address_verification_api_key is None:
            address_verification_api_key = os.environ.get("POSTGRID_ADDRESS_VERIFICATION_API_KEY")
        self.address_verification_api_key = address_verification_api_key

        if print_mail_api_key is None:
            print_mail_api_key = os.environ.get("POSTGRID_PRINT_MAIL_API_KEY")
        self.print_mail_api_key = print_mail_api_key

        if base_url is None:
            base_url = os.environ.get("POSTGRID_BASE_URL")
        if base_url is None:
            base_url = f"https://api.postgrid.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def address_verification(self) -> AddressVerificationResource:
        from .resources.address_verification import AddressVerificationResource

        return AddressVerificationResource(self)

    @cached_property
    def intl_address_verification(self) -> IntlAddressVerificationResource:
        from .resources.intl_address_verification import IntlAddressVerificationResource

        return IntlAddressVerificationResource(self)

    @cached_property
    def print_mail(self) -> PrintMailResource:
        from .resources.print_mail import PrintMailResource

        return PrintMailResource(self)

    @cached_property
    def with_raw_response(self) -> PostGridWithRawResponse:
        return PostGridWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostGridWithStreamedResponse:
        return PostGridWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._address_verification_api_key_auth, **self._print_mail_api_key_auth}

    @property
    def _address_verification_api_key_auth(self) -> dict[str, str]:
        address_verification_api_key = self.address_verification_api_key
        if address_verification_api_key is None:
            return {}
        return {"X-API-Key": address_verification_api_key}

    @property
    def _print_mail_api_key_auth(self) -> dict[str, str]:
        print_mail_api_key = self.print_mail_api_key
        if print_mail_api_key is None:
            return {}
        return {"X-API-Key": print_mail_api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.address_verification_api_key and headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        if self.print_mail_api_key and headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either address_verification_api_key or print_mail_api_key to be set. Or for one of the `X-API-Key` or `X-API-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        address_verification_api_key: str | None = None,
        print_mail_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            address_verification_api_key=address_verification_api_key or self.address_verification_api_key,
            print_mail_api_key=print_mail_api_key or self.print_mail_api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPostGrid(AsyncAPIClient):
    # client options
    address_verification_api_key: str | None
    print_mail_api_key: str | None

    def __init__(
        self,
        *,
        address_verification_api_key: str | None = None,
        print_mail_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPostGrid client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `address_verification_api_key` from `POSTGRID_ADDRESS_VERIFICATION_API_KEY`
        - `print_mail_api_key` from `POSTGRID_PRINT_MAIL_API_KEY`
        """
        if address_verification_api_key is None:
            address_verification_api_key = os.environ.get("POSTGRID_ADDRESS_VERIFICATION_API_KEY")
        self.address_verification_api_key = address_verification_api_key

        if print_mail_api_key is None:
            print_mail_api_key = os.environ.get("POSTGRID_PRINT_MAIL_API_KEY")
        self.print_mail_api_key = print_mail_api_key

        if base_url is None:
            base_url = os.environ.get("POSTGRID_BASE_URL")
        if base_url is None:
            base_url = f"https://api.postgrid.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def address_verification(self) -> AsyncAddressVerificationResource:
        from .resources.address_verification import AsyncAddressVerificationResource

        return AsyncAddressVerificationResource(self)

    @cached_property
    def intl_address_verification(self) -> AsyncIntlAddressVerificationResource:
        from .resources.intl_address_verification import AsyncIntlAddressVerificationResource

        return AsyncIntlAddressVerificationResource(self)

    @cached_property
    def print_mail(self) -> AsyncPrintMailResource:
        from .resources.print_mail import AsyncPrintMailResource

        return AsyncPrintMailResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPostGridWithRawResponse:
        return AsyncPostGridWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostGridWithStreamedResponse:
        return AsyncPostGridWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._address_verification_api_key_auth, **self._print_mail_api_key_auth}

    @property
    def _address_verification_api_key_auth(self) -> dict[str, str]:
        address_verification_api_key = self.address_verification_api_key
        if address_verification_api_key is None:
            return {}
        return {"X-API-Key": address_verification_api_key}

    @property
    def _print_mail_api_key_auth(self) -> dict[str, str]:
        print_mail_api_key = self.print_mail_api_key
        if print_mail_api_key is None:
            return {}
        return {"X-API-Key": print_mail_api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.address_verification_api_key and headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        if self.print_mail_api_key and headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either address_verification_api_key or print_mail_api_key to be set. Or for one of the `X-API-Key` or `X-API-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        address_verification_api_key: str | None = None,
        print_mail_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            address_verification_api_key=address_verification_api_key or self.address_verification_api_key,
            print_mail_api_key=print_mail_api_key or self.print_mail_api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PostGridWithRawResponse:
    _client: PostGrid

    def __init__(self, client: PostGrid) -> None:
        self._client = client

    @cached_property
    def address_verification(self) -> address_verification.AddressVerificationResourceWithRawResponse:
        from .resources.address_verification import AddressVerificationResourceWithRawResponse

        return AddressVerificationResourceWithRawResponse(self._client.address_verification)

    @cached_property
    def intl_address_verification(self) -> intl_address_verification.IntlAddressVerificationResourceWithRawResponse:
        from .resources.intl_address_verification import IntlAddressVerificationResourceWithRawResponse

        return IntlAddressVerificationResourceWithRawResponse(self._client.intl_address_verification)

    @cached_property
    def print_mail(self) -> print_mail.PrintMailResourceWithRawResponse:
        from .resources.print_mail import PrintMailResourceWithRawResponse

        return PrintMailResourceWithRawResponse(self._client.print_mail)


class AsyncPostGridWithRawResponse:
    _client: AsyncPostGrid

    def __init__(self, client: AsyncPostGrid) -> None:
        self._client = client

    @cached_property
    def address_verification(self) -> address_verification.AsyncAddressVerificationResourceWithRawResponse:
        from .resources.address_verification import AsyncAddressVerificationResourceWithRawResponse

        return AsyncAddressVerificationResourceWithRawResponse(self._client.address_verification)

    @cached_property
    def intl_address_verification(
        self,
    ) -> intl_address_verification.AsyncIntlAddressVerificationResourceWithRawResponse:
        from .resources.intl_address_verification import AsyncIntlAddressVerificationResourceWithRawResponse

        return AsyncIntlAddressVerificationResourceWithRawResponse(self._client.intl_address_verification)

    @cached_property
    def print_mail(self) -> print_mail.AsyncPrintMailResourceWithRawResponse:
        from .resources.print_mail import AsyncPrintMailResourceWithRawResponse

        return AsyncPrintMailResourceWithRawResponse(self._client.print_mail)


class PostGridWithStreamedResponse:
    _client: PostGrid

    def __init__(self, client: PostGrid) -> None:
        self._client = client

    @cached_property
    def address_verification(self) -> address_verification.AddressVerificationResourceWithStreamingResponse:
        from .resources.address_verification import AddressVerificationResourceWithStreamingResponse

        return AddressVerificationResourceWithStreamingResponse(self._client.address_verification)

    @cached_property
    def intl_address_verification(
        self,
    ) -> intl_address_verification.IntlAddressVerificationResourceWithStreamingResponse:
        from .resources.intl_address_verification import IntlAddressVerificationResourceWithStreamingResponse

        return IntlAddressVerificationResourceWithStreamingResponse(self._client.intl_address_verification)

    @cached_property
    def print_mail(self) -> print_mail.PrintMailResourceWithStreamingResponse:
        from .resources.print_mail import PrintMailResourceWithStreamingResponse

        return PrintMailResourceWithStreamingResponse(self._client.print_mail)


class AsyncPostGridWithStreamedResponse:
    _client: AsyncPostGrid

    def __init__(self, client: AsyncPostGrid) -> None:
        self._client = client

    @cached_property
    def address_verification(self) -> address_verification.AsyncAddressVerificationResourceWithStreamingResponse:
        from .resources.address_verification import AsyncAddressVerificationResourceWithStreamingResponse

        return AsyncAddressVerificationResourceWithStreamingResponse(self._client.address_verification)

    @cached_property
    def intl_address_verification(
        self,
    ) -> intl_address_verification.AsyncIntlAddressVerificationResourceWithStreamingResponse:
        from .resources.intl_address_verification import AsyncIntlAddressVerificationResourceWithStreamingResponse

        return AsyncIntlAddressVerificationResourceWithStreamingResponse(self._client.intl_address_verification)

    @cached_property
    def print_mail(self) -> print_mail.AsyncPrintMailResourceWithStreamingResponse:
        from .resources.print_mail import AsyncPrintMailResourceWithStreamingResponse

        return AsyncPrintMailResourceWithStreamingResponse(self._client.print_mail)


Client = PostGrid

AsyncClient = AsyncPostGrid
