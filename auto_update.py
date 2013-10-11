#!/usr/bin/env python

import os, sys
modulepath = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(modulepath)
if len(sys.argv)==3 and sys.argv[-2] == '--user':
    os.environ['USER'] = sys.argv[-1]
from generate_manifest import *
OLDMANIFEST = modulepath + '/default.xml'

if __name__ == '__main__':
    os.chdir(modulepath)
    os.system('git reset --hard')
    os.system('git pull')
    try:
        download_ignore_list()
    except:
        print 'Tizen git web page looks down'
        sys.exit(0)

    project_dict = download_project_list()
    projects = project_dict.keys()
    projects.sort()
    changes, report = changelog(projects)
    if changes == 0:
        print 'no changes'
        sys.exit(0)
    manifest = generate_manifest(project_dict)
    open('default.xml', 'w').write(manifest)
    cmd = 'git commit -a -F - <<EOF\nApplied to the changed repositories\n\n'\
            + report+'\nEOF'
    os.system(cmd)
    os.system('git push')

# vim: sw=4 ts=8 sts=4 et bs=2 fdm=marker fileencoding=utf8
