"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import re
import json
from typing import Callable, TypeVar, Optional, Generator, AsyncGenerator, Tuple
import httpx

T = TypeVar("T")


class ServerEvent:
    id: Optional[str] = None
    event: Optional[str] = None
    data: Optional[str] = None
    retry: Optional[int] = None


MESSAGE_BOUNDARIES = [
    b"\r\n\r\n",
    b"\n\n",
    b"\r\r",
]


async def stream_events_async(
    response: httpx.Response,
    decoder: Callable[[str], T],
    sentinel: Optional[str] = None,
) -> AsyncGenerator[T, None]:
    buffer = bytearray()
    position = 0
    discard = False
    async for chunk in response.aiter_bytes():
        # We've encountered the sentinel value and should no longer process
        # incoming data. Instead we throw new data away until the server closes
        # the connection.
        if discard:
            continue

        buffer += chunk
        for i in range(position, len(buffer)):
            char = buffer[i : i + 1]
            seq: Optional[bytes] = None
            if char in [b"\r", b"\n"]:
                for boundary in MESSAGE_BOUNDARIES:
                    seq = _peek_sequence(i, buffer, boundary)
                    if seq is not None:
                        break
            if seq is None:
                continue

            block = buffer[position:i]
            position = i + len(seq)
            event, discard = _parse_event(block, decoder, sentinel)
            if event is not None:
                yield event

        if position > 0:
            buffer = buffer[position:]
            position = 0

    event, discard = _parse_event(buffer, decoder, sentinel)
    if event is not None:
        yield event


def stream_events(
    response: httpx.Response,
    decoder: Callable[[str], T],
    sentinel: Optional[str] = None,
) -> Generator[T, None, None]:
    buffer = bytearray()
    position = 0
    discard = False
    for chunk in response.iter_bytes():
        # We've encountered the sentinel value and should no longer process
        # incoming data. Instead we throw new data away until the server closes
        # the connection.
        if discard:
            continue

        buffer += chunk
        for i in range(position, len(buffer)):
            char = buffer[i : i + 1]
            seq: Optional[bytes] = None
            if char in [b"\r", b"\n"]:
                for boundary in MESSAGE_BOUNDARIES:
                    seq = _peek_sequence(i, buffer, boundary)
                    if seq is not None:
                        break
            if seq is None:
                continue

            block = buffer[position:i]
            position = i + len(seq)
            event, discard = _parse_event(block, decoder, sentinel)
            if event is not None:
                yield event

        if position > 0:
            buffer = buffer[position:]
            position = 0

    event, discard = _parse_event(buffer, decoder, sentinel)
    if event is not None:
        yield event


def _parse_event(
    raw: bytearray, decoder: Callable[[str], T], sentinel: Optional[str] = None
) -> Tuple[Optional[T], bool]:
    block = raw.decode()
    lines = re.split(r"\r?\n|\r", block)
    publish = False
    event = ServerEvent()
    data = ""
    for line in lines:
        if not line:
            continue

        delim = line.find(":")
        if delim <= 0:
            continue

        field = line[0:delim]
        value = line[delim + 1 :] if delim < len(line) - 1 else ""
        if len(value) and value[0] == " ":
            value = value[1:]

        if field == "event":
            event.event = value
            publish = True
        elif field == "data":
            data += value + "\n"
            publish = True
        elif field == "id":
            event.id = value
            publish = True
        elif field == "retry":
            event.retry = int(value) if value.isdigit() else None
            publish = True

    if sentinel and data == f"{sentinel}\n":
        return None, True

    if data:
        data = data[:-1]
        event.data = data

        if (
            data.isnumeric()
            or data == "true"
            or data == "false"
            or data == "null"
            or data.startswith("{")
            or data.startswith("[")
            or data.startswith('"')
        ):
            try:
                event.data = json.loads(data)
            except Exception:
                pass

    out = None
    if publish:
        out = decoder(json.dumps(event.__dict__))

    return out, False


def _peek_sequence(position: int, buffer: bytearray, sequence: bytes):
    if len(sequence) > (len(buffer) - position):
        return None

    for i, seq in enumerate(sequence):
        if buffer[position + i] != seq:
            return None

    return sequence
