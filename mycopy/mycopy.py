import sys
import shutil

args = sys.argv[1:]
try:
    if len(args) != 3:
        raise Exception('명령어 형식이 올바르지않습니다')
    if args[0] != '-cp':
        raise Exception('알 수 없는 명령어입니다.')
except Exception as e:
    print(e)
else:
    src, dest = args[1], args[2]
    shutil.copyfile(src, dest)

