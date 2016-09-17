import tpfd

p = tpfd.Parser()

@p.on_recognize('The {noun} who say {thing}!')
def two_word_test(noun, thing):
    print (noun, thing)

def utf_parse1():
    p.parse_string('The ???? who say ??!')

def utf_parse2():
    p.parse_string('The ?? who say chipmunk!')

def utf_parse3():
    p.parse_string('The ? who say ??!')

if __name__ == '__main__':
    utf_parse1()
    utf_parse2()
    utf_parse3()