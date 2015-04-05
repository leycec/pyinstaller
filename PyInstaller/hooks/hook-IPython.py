#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


from PyInstaller.utils.hooks.hookutils import collect_data_files

#FIXME: Disabled, as this currently throws the following inscrutable exception:
#
#    Traceback (most recent call last):
#      File "<string>", line 1, in <module>
#      File "/usr/lib64/python3.3/site-packages/IPython/__init__.py", line 48, in <module>
#        from .core.application import Application
#      File "/usr/lib64/python3.3/site-packages/IPython/core/application.py", line 40, in <module>
#        from IPython.core import release, crashhandler
#      File "/usr/lib64/python3.3/site-packages/IPython/core/crashhandler.py", line 30, in <module>
#        from IPython.utils.sysinfo import sys_info
#      File "/usr/lib64/python3.3/site-packages/IPython/utils/sysinfo.py", line 101, in <module>
#        @py3compat.doctest_refactor_print
#      File "/usr/lib64/python3.3/site-packages/IPython/utils/py3compat.py", line 45, in wrapper
#        doc = str_change_func(doc)
#      File "/usr/lib64/python3.3/site-packages/IPython/utils/py3compat.py", line 125, in doctest_refactor_print
#        return _print_statement_re.sub(_print_statement_sub, doc)
#    TypeError: expected string or buffer
#    Traceback (most recent call last):
#      File "/usr/lib/python-exec/python3.3/pyinstaller", line 9, in <module>
#        load_entry_point('PyInstaller===3.0dev-be553f0-mod', 'console_scripts', 'pyinstaller')()
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/main.py", line 88, in run
#        run_build(opts, spec_file, pyi_config)
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/main.py", line 46, in run_build
#        PyInstaller.build.main(pyi_config, spec_file, **opts.__dict__)
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/build.py", line 1918, in main
#        build(specfile, kw.get('distpath'), kw.get('workpath'), kw.get('clean_build'))
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/build.py", line 1865, in build
#        exec(compile(open(spec).read(), spec, 'exec'))
#      File "freeze/betse.dir.spec", line 14, in <module>
#        exec(core_spec.read())
#      File "<string>", line 100, in <module>
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/build.py", line 356, in __init__
#        self.__postinit__()
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/build.py", line 215, in __postinit__
#        self.assemble()
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/build.py", line 636, in assemble
#        hook_name_space = mod_loader.load_module()
#      File "<frozen importlib._bootstrap>", line 584, in _check_name_wrapper
#      File "<frozen importlib._bootstrap>", line 1022, in load_module
#      File "<frozen importlib._bootstrap>", line 1003, in load_module
#      File "<frozen importlib._bootstrap>", line 560, in module_for_loader_wrapper
#      File "<frozen importlib._bootstrap>", line 868, in _load_module
#      File "<frozen importlib._bootstrap>", line 313, in _call_with_frames_removed
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/hooks/hook-IPython.py", line 16, in <module>
#        datas = collect_data_files('IPython')
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/utils/hooks/hookutils.py", line 624, in collect_data_files
#        pkg_base, pkg_dir = get_package_paths(package)
#      File "/usr/lib64/python3.3/site-packages/PyInstaller/utils/hooks/hookutils.py", line 546, in get_package_paths
#        assert is_package
#    AssertionError

# IPython (tested with 0.13) requires the following files:
#   ./site-packages/IPython/config/profile/README_STARTUP
# datas = collect_data_files('IPython')
