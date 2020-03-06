Powerline Nix
=============

A [Powerline] segment for **nix-shell** (one of the [Nix] tools). Similar to, and inspired by the stock [**virtualenv**
segment][virtualenv segment] although not quite as informative. The segment activates whenever in a **nix-shell**
session:

![demo]

Requirements
------------

Python 3 & Powerline for Python 3.

Installation
------------

Install the Python module. However you do it, it must end up in a place where Python can find it. You can try the
following as a diagnostic:

```bash
$ python3 -c 'from powerline_nix import nix_shell_segment; print(nix_shell_segment)'
<function nix_shell_segment at 0x7f871ba6d2f0>
```

Next, add a colorscheme to your config (see the [config instructions] for Powerline). For a look identical to the
**virtualenv** segment try the following:

```json
"nix_shell": { "fg": "white", "bg": "darkcyan", "attrs": [] }
```

Add the segment to your shell powerline and you should be good to go:

```json
{
    "function": "powerline-nix.nix_shell_segment",
    "priority": 50
}
```

If you have never customised your Powerline before, two configuration file models are provided. You can try placing them
at the following locations (pay attention to the file names):

 * `colorschemes-model.json` → `~/.config/powerline/colorschemes/default.json`
 * `shell-model.json` → `~/.config/powerline/themes/shell/default.json`

License
-------

Licensed under the MIT License. See the accompanying [LICENSE] file for details.

[Powerline]: https://powerline.readthedocs.io/en/latest/
[Nix]: https://nixos.org/nix/
[virtualenv segment]: http://powerline.readthedocs.io/en/master/configuration/segments/common.html#powerline.segments.common.env.virtualenv
[demo]: ./demo.png
[config instructions]: http://powerline.readthedocs.io/en/master/configuration.html
[LICENSE]: ./LICENSE
