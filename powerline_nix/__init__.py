from powerline.theme import requires_segment_info

@requires_segment_info
def nix_shell_segment(pl, segment_info, create_watcher=None):
    if segment_info['environ'].get('IN_NIX_SHELL', '') != '':
        return "(nix)"
