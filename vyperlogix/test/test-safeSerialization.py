from vyperlogix.oodb import *

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

if __name__ == "__main__":
    import sys
    sys.stdout.write( __copyright__+'\n')
    sys.stderr.write(__copyright__+'\n')

    try:
        import _psyco
        _psyco.importPsycoIfPossible()
        dumps = psyco.proxy(dumps)
        loads = psyco.proxy(loads)
    except ImportError:
        pass
    except NameError:
        pass

    value = (u'\N{POUND SIGN} Testing unicode', {True:False},[1,2,3,4],["simon"],("python is","cool"),
"pi equals",3.14,("longs are ok",
912398102398102938102398109238019283012983019238019283019283))
    data = dumps(value)
    print data
    print '-'*80
    x = loads(data)
    print x

