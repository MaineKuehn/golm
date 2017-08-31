import weakref
import rpconnect


class NameServer(object):
    """
    A nameserver to register and query slaves
    """
    def __init__(self):
        self._slaves = weakref.WeakSet()

    def add(self, name, port):
        """Register a node as available"""
        self._slaves.add((name, port))

    def discard(self, name, port):
        """Discard a previously available node"""
        self._slaves.discard((name, port))

    def get(self):
        """Get all currently available nodes"""
        # FIXME: return current state
        # TODO: have students search for this and file an issue
        return ['localhost']


class NameAPI(object):
    """
    Client API for a :py:class:`NameServer`

    .. code::

        api = NameClient('localhost', 8080)
        api.add(socket.gethostname(), 8080)
        peers = api.get()
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def add(self, name, port):
        return rpconnect.remote_call(self.host, self.port, 'nodes.add', name=name, port=port)

    def discard(self, name, port):
        return rpconnect.remote_call(self.host, self.port, 'nodes.add', name, port)

    def get(self):
        return rpconnect.remote_call(self.host, self.port, 'nodes.get')


def mount(rpc_server):
    nameserver = NameServer()
    rpc_server.register_payload(nameserver.add, name='nodes.add')
    rpc_server.register_payload(nameserver.discard, name='nodes.discard')
    rpc_server.register_payload(nameserver.get, name='nodes.get')
