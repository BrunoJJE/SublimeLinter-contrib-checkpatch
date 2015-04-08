SublimeLinter-contrib-checkpatch
================================

[![Build Status](https://travis-ci.org/BrunoJJE/SublimeLinter-contrib-checkpatch.svg?branch=master)](https://travis-ci.org/BrunoJJE/SublimeLinter-contrib-checkpatch)

This linter plugin for [SublimeLinter][docs] provides an interface to linux kernel [checkpatch.pl](http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/scripts/checkpatch.pl) tool. It will be used with files that have the “C” syntax (it won't work on “C++“ syntax).

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `checkpatch.pl` is installed on your system. To install `checkpatch.pl`, do the following:

1. Verify that perl is installed on your system by typing the following in a terminal :
   ```
   perl -v
   ```

1. Get the source of the linux kernel. You can for instance type the following in a terminal:
   ```
   git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
   ```

1. Put checkpatch.pl in your path. On linux, you can for instance create a symbolic link by typing something like the following in a terminal:
   ```
   sudo ln -s /path/to/kernel/source/tree/scripts/checkpatch.pl /usr/local/bin
   ```


**Note:** This plugin requires `checkpatch.pl` 0.32 or later.

### Linter configuration
In order for `checkpatch` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `checkpatch`, you can proceed to install the SublimeLinter-contrib-checkpatch plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `checkpatch`. Among the entries you should see `SublimeLinter-contrib-checkpatch`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-checkpatch provides its own settings.

|Setting|Description|
|:------|:----------|
|root|PATH to the kernel tree root.|

You must set this path to point to a valid kernel source tree (or you can add the “--no-tree“ in the `checkpatch` args setting, but in this case checkpatch won't be able to report all possible error/warning).

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
