import os

# Andrew Hassan specific code here
def get_short_path(cwd):
    result = []
    home = os.getenv('HOME')
    names = cwd.split(os.sep)
    if names[0] == '': names = names[1:]
    path = ''
    for i in range(len(names)):
        path += os.sep + names[i]
        if os.path.samefile(path, home):
            result = ['~'] + names[i+1:]
    result = names

    if len(result) > 3:
        result = [result[0]] + ["..."] + result[-2:]
    
    return result


def add_cwd_segment():
    cwd = powerline.cwd or os.getenv('PWD')
    names = get_short_path(cwd.decode('utf-8'))

    max_depth = powerline.args.cwd_max_depth
    if len(names) > max_depth:
        names = names[:2] + [u'\u2026'] + names[2 - max_depth:]

    if not powerline.args.cwd_only:
        for n in names[:-1]:
            powerline.append(' %s ' % n, Color.PATH_FG, Color.PATH_BG,
                    powerline.separator_thin, Color.SEPARATOR_FG)
    powerline.append(' %s ' % names[-1], Color.CWD_FG, Color.PATH_BG)

add_cwd_segment()
