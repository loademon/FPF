from src.factory.error import PrException
from src.utils.utils import (
    SearchScheme,
    ProxyScheme,
    SiteType,
    SUPPORTED_ADRESSES as supported_adresses,
)


class Proxy:
    def __init__(self, filters: SearchScheme) -> None:
        self.filters = filters

    def get_proxy_list(self) -> list[ProxyScheme]:
        """
        Returns a list of proxies that matches the specified parameters.
        Maybe proxies don't work. Must use something to check them.
        """
        fixed_proxies: list[ProxyScheme] = []
        adresses = self.__adresses_to_use(filters=self.filters)
        for adress in adresses:
            site_type = supported_adresses[adress]
            non_fixed_proxies: list[str] = self.__get_list_of_proxies(
                site_type=site_type
            )
            proxies = self.__fix_list_of_proxies(
                proxies=non_fixed_proxies, site_type=site_type
            )
            fixed_proxies = list(set(fixed_proxies + proxies))
        return fixed_proxies

    def __adresses_to_use(self, filters: SearchScheme) -> list[str]:
        adresses: list[str] = []
        if filters.protocol == "http":
            pass
        # TODO: write this function

    def __get_list_of_proxies(self, site_type: str = "hide-ip") -> list[str]:
        # TODO: get list of proxies
        pass

    def __fix_list_of_proxies(
        self, proxies: list[str], site_type: str = "hide-ip"
    ) -> list[ProxyScheme]:
        return getattr(SiteType, f"_{site_type.replace('-','_')}")(proxies=proxies)

    def __check_if_proxy_is_working(self, proxy: ProxyScheme) -> (bool, bool | None):
        # TODO: check if proxy is working
        pass
