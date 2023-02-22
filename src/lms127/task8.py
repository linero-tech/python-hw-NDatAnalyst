from to_do import TODO

def task8(sentence, character):
    result = sentence.count(character)
    return result
'''To inline or refactoring change to:-
 'return sentence.count(character)'''
if __name__ == "__main__":
    print(task8(sentence='I code in KOTLIN', character='I')) #2
    print(task8(sentence='I code in KOTLIN', character='i')) #1
    print(task8(sentence='I code in KOTLIN', character='k')) #0
    print(task8(sentence='I code in KOTLIN', character='K')) #1
    print(task8(sentence='I code in KOTLIN', character='z')) #0

