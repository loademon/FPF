from dataclasses import dataclass
from typing import Literal


@dataclass
class SearchScheme:
    protocol: str = None  # protocol of proxies to search for. Can be 'http', 'https', 'socks4' or 'socks5'. If None, proxies of all protocols will be returned
    country: str = None  # country code, like 'US'. If None, proxies from all countries will be returned
    elite: bool = (
        False  # if True, only elite proxies will be returned. Anonymity level: High
    )
    anonymous: bool = False  # if True, only anonymous proxies will be returned. Anonymity level: Medium
    timeout: float = 0.5  # timeout in seconds. If a proxy doesn't respond within this time, it will be skipped
    google: bool = False  # if True, only proxies that work with Google will be returned


@dataclass
class AdressScheme:  # supporting category information for providers
    url: str = ""
    http: bool = False
    https: bool = False
    socks4: bool = False
    socks5: bool = False
    country: str = None
    elite: bool = False
    anonymity: bool = False
    google: bool = False


@dataclass
class UrlScheme:
    http: str = ""
    https: str = ""
    socks4: str = ""
    socks5: str = ""


@dataclass
class ProxyScheme:
    anonymity: Literal[
        "elite", "anonymous", "transparent", None
    ] = None  # anonymity level
    protocol: Literal[
        "http", "https", "socks4", "socks5", None
    ] = None  # protocol of the proxy
    country: Literal["US", "UK", None] = None  # country code.
    host: str  # host of the proxy. Can be an IP or a domain
    port: int  # port of the proxy. Must be an integer
    google: bool  # if True, the proxy works with Google


class SiteType:
    def _hide_ip(proxies: list[str]) -> list[ProxyScheme]:
        # TODO: write this function
        pass

    def _PROXY_List(proxies: list[str]) -> list[ProxyScheme]:
        # TODO: write this function
        pass

    def _free_proxy_list(proxies: list[str]) -> list[ProxyScheme]:
        # TODO: write this function
        pass

    def _sslproxies(proxies: list[str]) -> list[ProxyScheme]:
        # TODO: write this function
        pass

    def _us_proxy(proxies: list[str]) -> list[ProxyScheme]:
        # TODO: write this function
        pass

    def _uk_proxy(proxies: list[str]) -> list[ProxyScheme]:
        # TODO: write this function
        pass


# SUPPORTED_ADRESSES: dict = [
#     "hide-ip",
#     "PROXY-List",
#     "free-proxy-list",
#     "sslproxies",
#     "us-proxy",
#     "uk-proxy",
# ]


SUPPORTED_ADRESSES: dict[str, AdressScheme] = {
    "hide-ip": AdressScheme(
        url=UrlScheme(
            http="",
            https="",
            socks4="",
            socks5="",
        ),
        http=True,
        https=True,
        socks4=True,
        socks5=True,
        country=None,
        elite=True,
        anonymity=True,
        google=True,
    ),
    "PROXY-List": AdressScheme(
        url=UrlScheme(
            http="",
            https="",
            socks4="",
            socks5="",
        ),
        http=True,
        https=False,
        socks4=True,
        socks5=True,
        country=None,
        elite=False,
        anonymity=False,
        google=True,
    ),
    # TODO: write other providers
}
