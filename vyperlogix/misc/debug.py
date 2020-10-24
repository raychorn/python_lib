import os,sys
from vyperlogix.misc.ObjectTypeName import typeClassName

__introspect__ = lambda o:['%s --> %s'%(a,type(o.__getattribute__(a))) for a in dir(o)]

__describe__ = lambda something,delim:'%s --> %s' % (typeClassName(something),delim.join(__introspect__(something)))

def introspect(something,fout=sys.stderr,delim='\n'):
    fout.write('='*40)
    fout.write('BEGIN: %s\n' % (something))
    fout.write('-'*40)
    fout.write(__describe__(something,delim))
    fout.write('-'*40)
    try:
        for item in something:
            if (item):
                fout.write('%s --> %s' % (item,__describe__(something,delim)))
    except:
        pass
    fout.write('END!!!')
    fout.write('='*40)

