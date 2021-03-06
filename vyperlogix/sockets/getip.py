from __future__ import print_function
__copyright__ = """\
(c). Copyright 2008-2020, Vyper Logix Corp., All Rights Reserved.

Published under Creative Commons License 
(http://creativecommons.org/licenses/by-nc/3.0/) 
restricted to non-commercial educational use only., 



THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
WITH THE USE OR PERFORMANCE OF THIS SOFTWARE !

USE AT YOUR OWN RISK.
"""

import sys
import socket
import struct

def get_ip_address(ifname):
    try:
        import fcntl
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
            )[20:24])
    except:
        import platform
        from vyperlogix import misc
        sys.stderr.write('%s.WARNING: Cannot use this function in %s.\n' % (misc.funcName(),platform.uname()[0]))
    return None

def get_ip_address_by_socket():
    return socket.gethostbyname(socket.gethostname())

if (__name__ == '__main__'):
    import platform
    from vyperlogix.misc import _utils
    if (_utils.isUsingWindows):
        sys.stderr.write('%s.WARNING: Cannot use this function in %s.\n' % (misc.funcName(),platform.uname()[0]))
    else:
        print(get_ip_address('eth0'))
    