"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from typing import (
    Any,
    Dict,
    List,
    Optional,
)
from httpx import Headers
from pydantic import BaseModel
from pydantic.fields import FieldInfo

from .metadata import (
    HeaderMetadata,
    find_field_metadata,
)

from .values import _populate_from_globals, _val_to_string


def get_headers(headers_params: Any, gbls: Optional[Any] = None) -> Dict[str, str]:
    headers: Dict[str, str] = {}

    globals_already_populated = []
    if headers_params is not None:
        globals_already_populated = _populate_headers(headers_params, gbls, headers, [])
    if gbls is not None:
        _populate_headers(gbls, None, headers, globals_already_populated)

    return headers


def _populate_headers(
    headers_params: Any,
    gbls: Any,
    header_values: Dict[str, str],
    skip_fields: List[str],
) -> List[str]:
    globals_already_populated: List[str] = []

    if not isinstance(headers_params, BaseModel):
        return globals_already_populated

    param_fields: Dict[str, FieldInfo] = headers_params.__class__.model_fields
    for name in param_fields:
        if name in skip_fields:
            continue

        field = param_fields[name]
        f_name = field.alias if field.alias is not None else name

        metadata = find_field_metadata(field, HeaderMetadata)
        if metadata is None:
            continue

        value, global_found = _populate_from_globals(
            name, getattr(headers_params, name), HeaderMetadata, gbls
        )
        if global_found:
            globals_already_populated.append(name)
        value = _serialize_header(metadata.explode, value)

        if value != "":
            header_values[f_name] = value

    return globals_already_populated


def _serialize_header(explode: bool, obj: Any) -> str:
    if obj is None:
        return ""

    if isinstance(obj, BaseModel):
        items = []
        obj_fields: Dict[str, FieldInfo] = obj.__class__.model_fields
        for name in obj_fields:
            obj_field = obj_fields[name]
            obj_param_metadata = find_field_metadata(obj_field, HeaderMetadata)

            if not obj_param_metadata:
                continue

            f_name = obj_field.alias if obj_field.alias is not None else name

            val = getattr(obj, name)
            if val is None:
                continue

            if explode:
                items.append(f"{f_name}={_val_to_string(val)}")
            else:
                items.append(f_name)
                items.append(_val_to_string(val))

        if len(items) > 0:
            return ",".join(items)
    elif isinstance(obj, Dict):
        items = []

        for key, value in obj.items():
            if value is None:
                continue

            if explode:
                items.append(f"{key}={_val_to_string(value)}")
            else:
                items.append(key)
                items.append(_val_to_string(value))

        if len(items) > 0:
            return ",".join([str(item) for item in items])
    elif isinstance(obj, List):
        items = []

        for value in obj:
            if value is None:
                continue

            items.append(_val_to_string(value))

        if len(items) > 0:
            return ",".join(items)
    else:
        return f"{_val_to_string(obj)}"

    return ""


def get_response_headers(headers: Headers) -> Dict[str, List[str]]:
    res: Dict[str, List[str]] = {}
    for k, v in headers.items():
        if not k in res:
            res[k] = []

        res[k].append(v)
    return res
