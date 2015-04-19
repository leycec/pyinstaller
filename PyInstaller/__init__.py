#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


__all__ = ('HOMEPATH', 'CONFIGDIR', 'PLATFORM',
           'VERSION', 'get_version')

import os
import sys


# Fail hard if Python does not have minimum required version
if sys.version_info < (2, 7):
    raise SystemExit('PyInstaller requires at least Python 2.7, sorry.')


# Extend PYTHONPATH with 3rd party libraries bundled with PyInstaller.
# (otherwise e.g. macholib won't work on Mac OS X)
from PyInstaller import lib
sys.path.insert(0, lib.__path__[0])


from PyInstaller import compat
from PyInstaller.compat import is_darwin, is_venv, is_win, is_py2
from PyInstaller.utils import git


#FIXME: Refactor to call our newly defined "hookutils" function.

# Fail hard if Python on Windows does not have pywin32 installed.
if is_win:
    try:
        import pywintypes  # One module from pywin32.
    except ImportError as exc:
        # print('sys.path: "{}".'.format(sys.path))
        # If the exception message resembles
        # "ImportError: No system module 'pywintypes' (pywintypes34.dll)",
        # attempt to manually find the referenced DLL and try again. This is a
        # well-known and currently unresolved issue with PyWin32.
        is_pywin32 = False
        if str(exc).startswith('No system module'):
            # Force PyWin32 to search "sys.path" for this DLL. By default,
            # PyWin32 only searches "sys.prefix", Windows system directories
            # (e.g., "C:\Windows\System32"), and the directory containing the
            # "win32.lib.pywintypes" module. That fails under modern Python
            # Windows installations, including Anaconda. This is a horrible
            # hack, but there literally exists no other way.
            sys.frozen = True

            # If running in a venv, the preferred site.getsitepackages()
            # function is unreliable. Fallback to searching "sys.path" instead.
            if is_venv:
                sys_paths = sys.path
            else:
                import site
                sys_paths = site.getsitepackages()

            for sys_path in sys_paths:
                # Absolute path of the directory possibly containing this DLL.
                pywin32_dll_dir = os.path.join(sys_path, 'pywin32_system32')

                if os.path.isdir(pywin32_dll_dir):
                    sys.path.append(pywin32_dll_dir)
                    # print('Testing "{}".'.format(pywin32_dll_dir))
                    try:
                        import pywintypes  # One module from pywin32.
                        is_pywin32 = True
                        break
                    except ImportError:
                        pass

            # Undo the above hack.
            del sys.frozen

        if not is_pywin32:
            raise SystemExit(
                'PyInstaller cannot check for assembly dependencies.\n'
                'Please install PyWin32.\n'
                'http://sourceforge.net/projects/pywin32/')


VERSION = (3, 0, 0, 'dev', git.get_repo_revision())


# This ensures for Python 2 that PyInstaller will work on Windows with paths
# containing foreign characters.
HOMEPATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if is_win and is_py2:
    try:
        unicode(HOMEPATH)
    except UnicodeDecodeError:
        # Do conversion to ShortPathName really only in case HOMEPATH is not
        # ascii only - conversion to unicode type cause this unicode error.
        try:
            import win32api
            HOMEPATH = win32api.GetShortPathName(HOMEPATH)
        except ImportError:
            pass


if is_win:
    CONFIGDIR = compat.getenv('APPDATA')
    if not CONFIGDIR:
        CONFIGDIR = os.path.expanduser('~\\Application Data')
elif is_darwin:
    CONFIGDIR = os.path.expanduser('~/Library/Application Support')
else:
    # According to XDG specification
    # http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
    CONFIGDIR = compat.getenv('XDG_DATA_HOME')
    if not CONFIGDIR:
        CONFIGDIR = os.path.expanduser('~/.local/share')
CONFIGDIR = os.path.join(CONFIGDIR, 'pyinstaller')


## Default values of paths where to put files created by PyInstaller.
# Folder where to put created .spec file.
DEFAULT_SPECPATH = compat.getcwd()
# Folder where to put created .spec file.
# Where to put the final app.
DEFAULT_DISTPATH = os.path.join(compat.getcwd(), 'dist')
# Where to put all the temporary work files, .log, .pyz and etc.
DEFAULT_WORKPATH = os.path.join(compat.getcwd(), 'build')


PLATFORM = compat.system() + '-' + compat.architecture()
# Include machine name in path to bootloader for some machines.
# e.g. 'arm'
if compat.machine():
    PLATFORM += '-' + compat.machine()


# path extensions for module seach
# FIXME this should not be a global variable
__pathex__ = []


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if len(VERSION) >= 4 and VERSION[3]:
        version = '%s%s' % (version, VERSION[3])
        # include git revision in version string
        if VERSION[3] == 'dev' and len(VERSION) >= 5 and len(VERSION[4]) > 0:
            version = '%s-%s' % (version, VERSION[4])
    return version
