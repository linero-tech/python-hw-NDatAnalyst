from to_do import TODO

#Inline
'''Refactoring: changing the implentation 
BUT keeping the behaviour, basically means
changing code but the outcome is
the same'''
def task7(sentence):
    result = len(sentence)
    return result

if __name__ == "__main__":
    print(task7(sentence='i like to fly'))
