import re


def mix(s1, s2):
    if s1 == s2:
        return ''
    result = []
    check_alp = '[a-z]'  # 正則
    base_letter_s1 = set(re.findall(check_alp, s1))  # 純小寫英文—無重複元素S1
    base_letter_s2 = set(re.findall(check_alp, s2))  # 純小寫英文—無重複元素S2
    only_s1_letter = base_letter_s1.difference(base_letter_s2)
    only_s2_letter = base_letter_s2.difference(base_letter_s1)


mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp")
