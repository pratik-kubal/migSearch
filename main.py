from multiprocessing import Process
import os
import subprocess
import sys
import time

def migrate():
	print('File Not found in local')
	print('Migrating process',os.getpid())
	time.sleep(3)
	subprocess.call(["./transfer.sh",cmdargs])
	time.sleep(3)

def local():
	print('Searching Local',os.getpid())
	time.sleep(3)
	subprocess.call(["./search.sh",cmdargs])
	my_path = "search.log"
	if os.path.getsize(my_path) > 0 :
		time.sleep(3)
		print('Found in Local\n No need to migrate')
	else :
		p=Process(target=migrate)
		p.start()
		p.join()
		print('Back to parent',os.getpid())
cmdargs = str(sys.argv[1])
local()

