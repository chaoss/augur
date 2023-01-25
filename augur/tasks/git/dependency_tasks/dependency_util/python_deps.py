import sys
import re
from pathlib import Path
<<<<<<< HEAD
import codecs
=======
>>>>>>> origin/andrew/test-user-api

def get_files(path):
	#copied from example on https://docs.python.org/3/library/pathlib.html
	dir = path
	p = Path(dir)
	files = list(p.glob('**/*.py'))
	return files
	
def get_deps_for_file(path):
<<<<<<< HEAD
	f = open(path, 'r',encoding="utf-8")

=======
	f = open(path, 'r')
>>>>>>> origin/andrew/test-user-api
	matches = re.findall("import\s*(\w*)", f.read())
	f.close()
	return matches
