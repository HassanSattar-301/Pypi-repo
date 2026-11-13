# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [ApimaticCalculatorTestClient](apimatic_calculator_test/client.py)

<details>
<summary><code>def calculate(operation: OperationTypeOrStr, x: float, y: float, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[float, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Calculates the expression using the specified operation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.calculate(OperationType.SUM, 1.5, 1.5)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type float
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.calculate(OperationType.SUM, 1.5, 1.5)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type float
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>operation</code> | <code>[OperationTypeOrStr](apimatic_calculator_test/models/enums/operation_type.py)</code> | The operator to apply on the variables |
| <code>x</code> | <code>float</code> | The LHS value |
| <code>y</code> | <code>float</code> | The RHS value |
| <code>request_options</code> | <code>[RequestOptionsOrDict](apimatic_calculator_test/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](apimatic_calculator_test/core/results.py)&#91;float, [RawError](apimatic_calculator_test/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>float</code>

**On `Failure`**: `error` is <code>[RawError](apimatic_calculator_test/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

