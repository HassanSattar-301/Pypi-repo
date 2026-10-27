<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `apimatic_calculator/client.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.calculate

- **Route**: `GET /{operation}`
- **Signature**: `def calculate(operation: OperationTypeOrStr, x: float, y: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `operation`, `x`, `y`
- **Params**: `operation` — path · `x` — query · `y` — query
- **Returns (parsed)**: `float`
- **Returns (raw)**: `ApiResult[float, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OperationTypeOrStr` | `apimatic_calculator/models/enums/operation_type.py` |

