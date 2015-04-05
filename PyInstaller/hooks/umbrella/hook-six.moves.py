#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.


from PyInstaller.utils.hooks import hookutils

# TODO We should also account for packages embedding "six.moves" within their
# package tree, including: "ecdsa.six.moves", "scipy.lib.six.moves". To do so,
# shift the body of this function into a new hook utility function.

def hook(mod):
    trg_mod_statement = """
import six

# The "MovedModule" object for such source module or None if such module was
# actually a moved attribute.
moved_module = six._importer.known_modules.get(%s)

# If such source module is a moved module, print the name of the corresponding
# target module; else, print the empty string.
print(getattr(moved_module, 'mod', ''))
"""

    # "."-delimited name of the target module mapped to by "six", where
    # "mod.name" is the "."-delimited name of the source module requested from
    # the fake "six.moves" module (e.g., "six.moves.tkinter").
    trg_mod = hookutils.exec_statement(trg_mod_statement % mod.name)

    # If such module is actually a moved module rather than a moved attribute,
    # add such module as a dependency of the passed fake module.
    if trg_mod:
        hookutils.logger.debug('Mapped "%s" to "%s".', mod.name, trg_mod)
        mod.add_import(trg_mod)

    return mod
