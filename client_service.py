import functools
import xmlrpclib
import pdb
HOST = 'localhost'
PORT = 8069
DB = 'test'
USER = 'admin'   #not db username and password  but odoo db username and  password
PASS = 'test'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login


uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid: %d)" % (USER,uid)



call = functools.partial(
	xmlrpclib.ServerProxy(ROOT + 'object').execute,
	DB, uid, PASS)
	
# 2. Read the sessions
	
sessions = call('openacademy.session','search_read', [], ['name', 'seats'])
for session in sessions:
    print "Session %s (%d seats)" % (session['name'], session['seats'])
	
	
# 3.create a new session
session_id = call('openacademy.session', 'create', {
    'name' : 'My session test',
    'course_id' : 2,
})
