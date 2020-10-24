import os, sys, traceback, re

from vyperlogix import misc
from vyperlogix.hash import lists
from vyperlogix.misc import ObjectTypeName

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

from vyperlogix.sf.abstract import SalesForceAbstract

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

class SalesForceLeadSourceHistory(SalesForceAbstract):
    def __init__(self, sfQuery):
	super(SalesForceLeadSourceHistory, self).__init__(sfQuery, object_name='LeadSourceHistory__c')
	
    def new_schema(self,LeadSource__c,RecordTypeId__c,Contact__c=None,Lead__c=None):
	'''This method builds a schema that can be used to make a new instance of this object via a Factory.'''
	return {'Contact__c': Contact__c,
		'Lead__c': Lead__c,
		'LeadSource__c': LeadSource__c,
		'RecordTypeId__c': RecordTypeId__c
		}

    def soql_getHistoryByLeadOrContact():
        doc = "soql for getHistoryByLeadOrContact()"
        def fget(self):
            return "Select l.Contact__c, l.Lead__c, l.LeadSource__c, l.RecordTypeId__c from LeadSourceHistory__c l WHERE ( (l.Contact__c = '%s') OR (l.Lead__c = '%s') )"
        return locals()
    soql_getHistoryByLeadOrContact = property(**soql_getHistoryByLeadOrContact())

    def getActivityByLeadOrContactId(self,id):
	soql = self.soql_getHistoryByLeadOrContact % (id,id)
	histories = self.sf_query(soql)
	return histories
    
if __name__ == "__main__":
    import sys
    sys.stdout.write( __copyright__+'\n')
    sys.stderr.write(__copyright__+'\n')
