"""Formatting Utilities."""

# Standard Library
from typing import Union
from ipaddress import IPv4Address, IPv6Address, ip_address


def format_listen_address(listen_address: Union[IPv4Address, IPv6Address, str]) -> str:
    """Format a listen_address for Gunicorn."""
    fmt = str(listen_address)

    if isinstance(listen_address, str):
        try:
            listen_address = ip_address(listen_address)
        except ValueError:
            pass

    if (
        isinstance(listen_address, (IPv4Address, IPv6Address))
        and listen_address.version == 6
    ):
        fmt = f"[{str(listen_address)}]"

    return fmt
