import argparse
import rpconnect

from . import ping
from . import server_tools
from . import nameserver


CLI = argparse.ArgumentParser('Start a GOL server')
CLI.add_argument(
    '-p', '--port',
    help='port to listen on',
    default=8080,
    type=int,
)
CLI.add_argument(
    '-i', '--interface',
    help='interface to bind to, e.g. localhost',
    default='',
)

options = CLI.parse_args()
with rpconnect.RpcServer(port=options.port, interface=options.interface) as rpc_server:
    ping.mount(rpc_server)
    server_tools.mount(rpc_server)
    nameserver.mount(rpc_server)
    rpc_server.run()
