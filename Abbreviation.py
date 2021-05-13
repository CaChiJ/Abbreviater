def GetAbbreviatePoint(text):
    result = []

    #case 1 : 선어말 어미, 부사, 명사형 축약
    REMOVED_SPACE = ' _ '
    replaceTable = [['하여', '해', 1], ['하였', '했', 1], ['되어', '돼', 1], ['되었', '됐', 1], ['었었', '었', 1], ['했었', '했', 1], ['보았', '봤', 1], ['주었', '줬', 1], [' 매우 ', REMOVED_SPACE, 3], [' 아주 ', REMOVED_SPACE, 3], [' 굉장히 ', REMOVED_SPACE, 3], [' 정말 ', REMOVED_SPACE, 3], [' 약간 ', REMOVED_SPACE, 3], [' 결코 ', REMOVED_SPACE, 3], [' 조금 ', REMOVED_SPACE, 3], ['다는 것', '(으)ㅁ', 3], ['와 같은 ', ' 같은 ', 1], ['와 같이', ' 같이 ', 1], ['게 되었', '었/였/았', 3], ['게 됐', '었/였/았', 2]]
    passCount = 0

    for idx in range(len(text)):
        if passCount > 0:
            passCount -= 1
            continue

        for rep in replaceTable:
            if idx + len(rep) >= len(text):
                continue

            flag = False;

            for replaceLetter, letter in zip(rep[0], text[idx:]):
                if replaceLetter != letter:
                    flag = True
                    break

            if flag:
                continue

            result.append((idx, len(rep[0]), rep[1], rep[2]))
            passCount = len(rep[0]) - 1
            break

    return result
