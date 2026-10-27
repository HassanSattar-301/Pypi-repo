from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .base_client import DEFAULT_TIMEOUT, BaseApimaticCalculatorClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiResult,
    BaseRawResponse,
    HttpClient,
    Httpx2Client,
    LoggingOptionsOrDict,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RetryOptionsOrDict,
    param,
    raw_error_response,
    text_decoder,
    unwrap,
)
from .models.enums.operation_type import OperationTypeOrStr
from .server.server import Server


class ApimaticCalculatorClient(BaseApimaticCalculatorClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
    ) -> None:
        super().__init__(
            base_url=base_url, timeout=timeout, retry_options=retry_options, logging_options=logging_options
        )
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
            retry_options=self._retry_options,
            logging_options=self._logging_options,
            global_headers=[
                param[str]("User-Agent", "ApimaticCalculatorClient/2.3 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "2.3"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )

    @cached_property
    def with_raw_response(self) -> ApiWithRawResponse:
        return ApiWithRawResponse(self._raw_client, self._server)

    def calculate(
        self, operation: OperationTypeOrStr, x: float, y: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> float:
        """Calculates the expression using the specified operation.

        Args:
            operation: The operator to apply on the variables
            x: The LHS value
            y: The RHS value
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The result of the calculation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self.with_raw_response.calculate(operation, x, y, request_options=request_options))

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


class ApiWithRawResponse(BaseRawResponse[RawClient, Server]):
    def calculate(
        self, operation: OperationTypeOrStr, x: float, y: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[float, RawError]:
        """Calculates the expression using the specified operation.

        Args:
            operation: The operator to apply on the variables
            x: The LHS value
            y: The RHS value
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/{operation}"),
            path_params=[param[OperationTypeOrStr]("operation", operation)],
            query_params=[param[float]("x", x), param[float]("y", y)],
            decoder=text_decoder[float],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


Client = ApimaticCalculatorClient
