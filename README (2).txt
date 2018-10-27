Simple Web Scraper

BEFORE YOU START THE SCRIPT

For this script to run you will need:

install python 3.6.5:
for 64bit system : https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe

for x86 system: https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe

IMPORTANT:
While installing pyhton YOU MUST CHECK BOX when it says ADD PYTHON TO PATH!!! LIKE IMPORTANT.jpg!!!



install python bs4 using cmd and write this
pip install bs4

install selenium using cmd:
pip install selenium


install firefox installe ( INSTALL IT IN DEFAULT FOLDER!!!)
https://www.mozilla.org/sr/firefox/download/thanks/

===================================================
To run the script, plase tsv file with your numbers in folder where the script is.
then
just run the script u-win.py

Windows using cmd:
python usb.py

Linux using terminal:
./usb-win.py

by milemik :D


C:\Users\PME>cd C:\Users\PME\Desktop\ib tracking\Usbs.com

C:\Users\PME\Desktop\ib tracking\Usbs.com>dir
 Volume in drive C has no label.
 Volume Serial Number is 46E6-E118

 Directory of C:\Users\PME\Desktop\ib tracking\Usbs.com

07/02/2018  09:05 PM    <DIR>          .
07/02/2018  09:05 PM    <DIR>          ..
06/15/2018  10:57 PM        12,834,953 geckodriver.exe
06/29/2018  10:45 PM            64,189 IMPORTANT.jpg
07/01/2018  08:14 PM               860 README.txt
07/02/2018  09:05 PM               678 sample input.txt
06/29/2018  11:09 PM             4,101 usb-win.py
               5 File(s)     12,904,781 bytes
               2 Dir(s)  161,204,019,200 bytes free

C:\Users\PME\Desktop\ib tracking\Usbs.com>python
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)]
 on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

C:\Users\PME\Desktop\ib tracking\Usbs.com>pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependen
cies.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be
                              used up to 3 times (corresponding to WARNING,
                              ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should
                              attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host as trusted, even though it does
                              not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.

C:\Users\PME\Desktop\ib tracking\Usbs.com>python usb-win.py
Traceback (most recent call last):
  File "usb-win.py", line 3, in <module>
    from bs4 import BeautifulSoup as bs
ModuleNotFoundError: No module named 'bs4'

C:\Users\PME\Desktop\ib tracking\Usbs.com>pip install bs4
Collecting bs4
  Downloading https://files.pythonhosted.org/packages/10/ed/7e8b97591f6f45617413
9ec089c769f89a94a1a4025fe967691de971f314/bs4-0.0.1.tar.gz
Collecting beautifulsoup4 (from bs4)
  Downloading https://files.pythonhosted.org/packages/9e/d4/10f46e5cfac773e22707
237bfcd51bbffeaf0a576b0a847ec7ab15bd7ace/beautifulsoup4-4.6.0-py3-none-any.whl (
86kB)
    100% |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 92kB 2.0MB/s
Installing collected packages: beautifulsoup4, bs4
  Running setup.py install for bs4 ... done
Successfully installed beautifulsoup4-4.6.0 bs4-0.0.1
You are using pip version 9.0.1, however version 10.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' comm
and.

C:\Users\PME\Desktop\ib tracking\Usbs.com>pip install selenium
Collecting selenium
  Downloading https://files.pythonhosted.org/packages/41/c6/78a9a0d0150dbf43095c
6f422fdf6f948e18453c5ebbf92384175b372ca2/selenium-3.13.0-py2.py3-none-any.whl (9
46kB)
    100% |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 952kB 1.0MB/s
Installing collected packages: selenium
Successfully installed selenium-3.13.0
You are using pip version 9.0.1, however version 10.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' comm
and.

C:\Users\PME\Desktop\ib tracking\Usbs.com>python usb-win.py
Enter the name of tsv fail, without tsv file extend
Traceback (most recent call last):
  File "usb-win.py", line 116, in <module>
    nolet_list, let_list, id_send, idn_send = get_num_from_text()
  File "usb-win.py", line 16, in get_num_from_text
    file_name = input('Enter the name of tsv fail, without tsv file extend\n')
KeyboardInterrupt

C:\Users\PME\Desktop\ib tracking\Usbs.com>report-56295017711
'report-56295017711' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\PME\Desktop\ib tracking\Usbs.com>



