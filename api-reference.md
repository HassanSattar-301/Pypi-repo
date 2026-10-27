# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [ApimaticCalculatorClient](apimatic_calculator/client.py)

<details>
<summary><code>def calculate(operation: OperationTypeOrStr, x: float, y: float, *, request_options: RequestOptionsOrDict | None = None) -> float</code></summary>

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
try:
    response = client.calculate(OperationType.SUM, 4, 5)
    # TODO: Handle 'response' of type float
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calculate(OperationType.SUM, 4, 5)
    # TODO: Handle 'response' of type float
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>operation</code> | <code>[OperationTypeOrStr](apimatic_calculator/models/enums/operation_type.py)</code> | The operator to apply on the variables |
| <code>x</code> | <code>float</code> | The LHS value |
| <code>y</code> | <code>float</code> | The RHS value |
| <code>request_options</code> | <code>[RequestOptionsOrDict](apimatic_calculator/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>float</code> -- The result of the calculation

**OnError**: <code>[ApiError](apimatic_calculator/core/exceptions.py)&#91;[RawError](apimatic_calculator/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

