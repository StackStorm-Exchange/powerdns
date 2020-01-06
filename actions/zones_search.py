from lib.base import PowerDNSClient


class ZonesSearch(PowerDNSClient):
    """
    Search for a term in all zones on the server.
    """
    def run(self, server_id, search_term, max_results=50, response_timeout=5):
        super().run(response_timeout)
        return (True, self.search(server_id, search_term, max_results))
