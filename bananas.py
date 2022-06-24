"""
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.
(Используйте - для обозначения зачеркнутой буквы)
Input: bbananana
Output:
b-anana--
b-anan--a
b-ana--na
b-an--ana
b-a--nana
b---anana
-banana--
-banan--a
-bana--na
-ban--ana
-ba--nana
-b--anana
"""


def bananas(s, word='banana'):
    ret = []

    if word == '':
        ret.append(''.rjust(len(s), '-'))
        return ret

    for si in range(len(s)):
        if word[0] == s[si]:
            left_s = ''.rjust(si, '-') + s[si]

            if s[si + 1:] == '' and word[1:] == '':
                ret.append(left_s)

            else:
                right_s_list = bananas(s[si + 1:], word[1:])
                for right_s in right_s_list:
                    ret.append(left_s + right_s)

    return set(ret)


"""
Для проверки:

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
"""
