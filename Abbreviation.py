def GetAbbreviatePoint(text):
    result = []

    #case 1 : 선어말 어미 축약
    replaceTable = [['하였', '했'], ['되었', '됐'], ['었었', '었'], ['했었', '했'], ['보았', '봤'], ['주었', '줬'], [' 매우 ', ' '], [' 아주 ', ' '], ['굉장히', ' '], [' 정말 ', ' '], [' 약간 ', ' ']]
    for idx in range(len(text)):
        for rep in replaceTable:
            flag = False;

            for i, letter in enumerate(rep[0]):
                if idx + i >= len(text) or text[idx + i] != letter:
                    flag = True
                    break

            if flag:
                continue

            result.append([idx, len(rep[0]), rep[1]])
            break

    return result
