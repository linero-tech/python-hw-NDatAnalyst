from to_do import TODO


def task9(sentence, character):
    return character.lower() in sentence.lower()

if __name__ == "__main__":
    print(task9(sentence="I code in KOTLIN", character='i')) #true
    print(task9(sentence='I code in KOTLIN', character='I'))#true
    print(task9(sentence='I code in KOTLIN', character='k')) #true
    print(task9(sentence='I code in KOTLIN', character='K')) #true
    print(task9(sentence='I code in KOTLIN', character='z')) #false