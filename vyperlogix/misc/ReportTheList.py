from __future__ import print_function
import sys

def reportTheList(l,title,callback=None,asCSV=False,fOut=sys.stdout):
    '''Report the List using a callback or asCSV or the default str(item) method.'''
    from vyperlogix.hash import lists
    from vyperlogix.parsers import CSV
    from vyperlogix import misc
    from vyperlogix.misc import ObjectTypeName

	fOut.write('BEGIN: %s num=(%s)\n' % (title,len(l)))
	i = 1
	if (misc.isIterable(l)) or (misc.isList(l)):
		for item in l:
			if (isinstance(item,tuple)):
				item = list(item)
			if (isinstance(item,list)):
				if (lists.isDict(item[0])):
					lists.prettyPrint(item[0],title='%d :: %s' % (i,title),asCSV=asCSV,fOut=fOut)
					i += 1
				else:
					isHandled = False
					if (callable(callback)):
						try:
							fOut.write('\t%s\n' % (callback(item[0])))
							isHandled = True
						except:
							pass
					if (not isHandled):
						if (asCSV):
							fOut.write('%s\n' % (CSV.asCSV(item)))
						else:
							fOut.write('\t%s\n' % (item[0]))
					i += 1
				for _item in item[1:]:
					if (misc.isList(_item)):
						for __item in _item:
							if (lists.isDict(__item)):
								lists.prettyPrint(__item,title='%d :: %s' % (i,title),asCSV=asCSV,fOut=fOut)
								i += 1
							else:
								isHandled = False
								if (callable(callback)):
									try:
										fOut.write('\t\t%d :: %s\n' % (ii,callback(__item)))
										isHandled = True
									except:
										pass
								if (not isHandled):
									if (asCSV):
										fOut.write('"%d","%s"\n' % (ii,__item))
									else:
										fOut.write('\t\t%d :: %s\n' % (ii,__item))
							i += 1
					else:
						if (lists.isDict(_item)):
							lists.prettyPrint(_item,title='%d :: %s' % (i,title),asCSV=asCSV,fOut=fOut)
							i += 1
						else:
							isHandled = False
							if (callable(callback)):
								try:
									fOut.write('\t\t%s\n' % (callback(__item)))
									isHandled = True
								except:
									pass
							if (not isHandled):
								if (asCSV):
									fOut.write('"%s"\n' % (_item))
								else:
									fOut.write('\t\t%s\n' % (_item))
								i += 1
			else:
				if (lists.isDict(item)):
					lists.prettyPrint(item,title='%d :: %s' % (i,title),asCSV=asCSV,fOut=fOut)
					i += 1
				else:
					isHandled = False
					if (callable(callback)):
						try:
							fOut.write('\t%d :: %s\n' % (i,callback(item)))
							isHandled = True
						except:
							pass
					if (not isHandled):
						if (asCSV):
							fOut.write('"%d","%s"\n' % (i,item))
						else:
							fOut.write('\t%d :: %s\n' % (i,item))
						i += 1
		else:
			fOut.write('NOTHING TO REPORT, List is EMPTY or not an interable; just for the record type "%s" is not iterable.\n' % (ObjectTypeName.typeClassName(l)))
			fOut.write('END! %s\n' % (title))
