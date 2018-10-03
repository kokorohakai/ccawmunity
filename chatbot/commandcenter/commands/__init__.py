from os import listdir
from os.path import isfile, dirname, abspath, join

commandFiles = []
moduleNames = []

# make a list of python files in the package directory.
# remove __init__.py from the list.
dir = dirname( abspath( __file__ ) )

for f in listdir( dir ):
    if f.endswith(".py") and f!="__init__.py" and isfile(dir + "/"+f):
        commandFiles.append( dir + f )
        moduleNames.append(f[0:-3])

__all__ = moduleNames
