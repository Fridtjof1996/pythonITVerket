#!c:\users\eier\documents\pythonblackjack\blackjack\python\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'blackjack','console_scripts','play'
__requires__ = 'blackjack'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('blackjack', 'console_scripts', 'play')()
    )
