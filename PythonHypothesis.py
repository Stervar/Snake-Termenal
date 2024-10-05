# Пример:

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst

def decode(lst):
    q = ''
    for character, count in lst:
          q += character * count
    return q

## Мы хотим написать тест для этой пары функций, который проверит некоторый инвариант из их должностных обязанностей.


## Инвариант, когда у вас есть такого рода encoding/decoding заключается в том, что если вы кодируете что-то, а затем декодируете это, то получаете то же самое значение назад.


## Давайте посмотрим, как это можно сделать с помощью Hypothesis:


from hypothesis import given
from hypothesis.strategies import text, characters

@given(text(alphabet=characters(whitelist_categories=('Ll', 'Lu', 'Nd')), min_size=1))
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s



## Мы хотим написать тест для этой пары функций, который проверит некоторый инвариант из их должностных обязанностей.


## Инвариант, когда у вас есть такого рода encoding/decoding заключается в том, что если вы кодируете что-то, а затем декодируете это, то получаете то же самое значение назад.


## Давайте посмотрим, как это можно сделать с помощью Hypothesis:





    