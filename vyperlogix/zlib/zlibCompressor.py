import gzip, zlib, base64

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

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

def decompress_zlib(s):
    return zlib.decompress(base64.decodestring(s), 15)

def zlib_compress(s):
    return base64.encodestring(zlib.compress(s, 9))
