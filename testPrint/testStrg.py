import os

pathFolderStorage = '/home/sergey/Grunt1911'

total_size = 0
for dirpath, dirnames, filenames in os.walk(pathFolderStorage):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    # skip if it is symbolic link
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)

size = total_size

print(size)
