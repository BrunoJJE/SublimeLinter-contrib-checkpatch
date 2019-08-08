#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Bruno JJE
# Copyright (c) 2015 Bruno JJE
#
# License: MIT
#

"""This module exports the Checkpatch plugin class."""

from SublimeLinter.lint import Linter


class Checkpatch(Linter):

    """Provides an interface to linux kernel 'checkpatch.pl' tool."""

    cmd = 'checkpatch.pl -f @'
    executable = None
    version_re = r'Version: (?P<version>\d+\.\d+)'
    version_requirement = '>= 0.32'
    multiline = True
    tempfile_suffix = 'c'

    defaults = {
        '--root=': '/path/to/kernel/source/tree',
        'selector': 'source.c, source.h'
    }

    # Here is several sample error/warning output:
    # ----8<------------
    # ERROR: space prohibited before that close parenthesis ')'
    # #6: FILE: coding_style.c:6:
    # +int do_work( int * my_int, int retval ) {
    # ----8<------------
    # ERROR: space required after that ';' (ctx:VxO)
    # #11: FILE: coding_style.c:11:
    # +   for(x=0;x< * my_int;++x) {
    #                        ^
    # ----8<------------
    # WARNING: printk() should include KERN_ facility level
    # #17: FILE: coding_style.c:17:
    # +       printk("We slept a long time!");
    # ----8<------------
    # WARNING: Missing a blank line after declarations
    # #9: FILE: helloworld.c:9:
    # +   int y = 3;
    # +   pr_debug("Hello World!\n");
    # ----8<------------

    regex = (
        r"^(?:(?P<error>ERROR)|(?P<warning>WARNING)):\s(?P<message>[^\n]*)\n"
        r"#(?P<linebis>[0-9]+): FILE: (?P<path>.*):(?P<line>[0-9]+):\n"
        r"(?P<code>(^\+[^\n]+)+\n)?"
        r"((?P<align> )(?P<col>[^\^]*)[\^]+)?"
    )

    def split_match(self, match):
        """Extract and return values from match."""
        match, line, col, error, warning, message, near = super().split_match(match)

        if match:
            if error:
                message = "ERROR: " + message
            if warning:
                message = "WARNING: " + message

        return match, line, col, error, warning, message, near
