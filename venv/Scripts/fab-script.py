#!C:\Users\QAQ\PycharmProjects\py3\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Fabric==1.14.0','console_scripts','fab'
__requires__ = 'Fabric==1.14.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Fabric==1.14.0', 'console_scripts', 'fab')()
    )
