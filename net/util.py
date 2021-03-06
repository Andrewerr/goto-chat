import socket
import struct
from ipaddress import IPv4Network
from threading import Lock

LOCK=Lock()

from core.config import NET_DATA, DEFAULT_ENCODING


def get_broadcast():
    net = IPv4Network(NET_DATA, False)
    return str(net.broadcast_address)


def ip2bytes(ip: str):
    _ip = struct.unpack('BBBB', socket.inet_aton(ip))
    s = ""
    for x in _ip:
        s += chr(x)
    return bytes(s, DEFAULT_ENCODING)


def local_ip():
    return socket.gethostbyname(socket.gethostname())


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def bytes2int4(x: bytes):
    assert len(x) == 4
    return struct.unpack("<L", x)[0]


def int42bytes(i: int):
    return struct.pack(">I", i)

def lock(fn):
    def wrap(*args,**kwargs):
        LOCK.acquire()
        fn(*args,**kwargs)
        LOCK.release()
    return wrap