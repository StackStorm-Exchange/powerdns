from lib.base import PowerDNSClient


class ZoneDelete(PowerDNSClient):
    """
    Delete a zone by name.
    """
    def run(self, server_id, name, response_timeout=5):
        super().run(response_timeout)
        return (True, self.zone_delete(server_id, name))
