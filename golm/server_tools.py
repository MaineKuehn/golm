import rpconnect
import logging
import inspect


class PayloadStore(object):
    def __init__(self, server):
        self._server = server

    def get_payloads(self):
        return {name: inspect.signature(obj) for name, obj in self._server._payloads.values()}


def set_logging(name='', level='DEBUG'):
    level = getattr(logging, level, level)
    logging.getLogger(name).setLevel(level)


def mount(rpc_server):
    payload_info = PayloadStore(rpc_server)
    rpc_server.register_payload(payload_info.get_payloads, name='get_payloads')
    rpc_server.register_payload(set_logging, name='set_logging')
