from to_do import TODO


def task10_1(assessments):
    return len(assessments)

def task10_2(assessments):
    return assessments[3]


def task10_3(assessments):
    return assessments[len(assessments) // 2]


def task10_4(assessments):
    return assessments[0:3]

if __name__ == "__main__":
    print(task10_1('lmhf')) #4
    print(task10_2('lmhf')) #f
    print(task10_3('lmuhf')) #u
    print(task10_4('lmhf')) #lmh
