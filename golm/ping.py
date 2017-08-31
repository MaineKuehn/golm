import rpconnect


def ping(host, port):
    try:
        return rpconnect.remote_call(host, port, 'ping')
    except Exception:
        return False


def pingserv():
    return True


def mount(rpc_server):
    rpc_server.register_payload(pingserv, name='ping')
