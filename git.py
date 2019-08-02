import os
import sys


def exec_command(command):
    result = os.popen(command)
    return ''.join(result.readlines())


dirs = [path for path in os.listdir('.') if os.path.isdir(path)]
argv = ' '.join(sys.argv[1:])
git_command = 'git' + argv
for d in dirs:
    print '===========================%s================================' % d
    print exec_command('cd %s && %s' % (d, git_command))
