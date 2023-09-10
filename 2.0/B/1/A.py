task_code = int(input())
iter_verd = int(input())
checker_verd = int(input())
if iter_verd == 0:
    if task_code != 0:
        print(3)
    else:
        print(checker_verd)
elif iter_verd == 1:
    print(checker_verd)
elif iter_verd == 4:
    if task_code != 0:
        print(3)
    else:
        print(4)
elif iter_verd == 6:
    print(0)
elif iter_verd == 7:
    print(1)
else:
    print(iter_verd)
