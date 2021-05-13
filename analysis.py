#!/usr/bin/python3
print("Content-Type: text/html; charset=utf-8")
print()
import sys
import codecs
import cgi
import Abbreviation as ab

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

inputText = cgi.FieldStorage()['inputText'].value + ' '
result = ab.GetAbbreviatePoint(inputText)
result.append([-1, -1, ""])

pagePiece = ['''
<!DOCTYPE html>
<html>
<head>
  <title>텍스티 - 분석 결과</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6435868338048324"
     crossorigin="anonymous"></script>
</head>
<body>
  <h3 align="center">분석 결과</h3>
  <div class="inline-container">
    <div id="text-display">
        ''', '''
    </div>
  </div>
  <div align="right">
''', '''
  </div>
</body>
<footer>
  <h5 align="center" id="madeby-information">made by CaChiJ</h5>
  <h5 align="center" id="contact-information">contact : chj7239@gmail.com | https://github.com/CaChiJ/Abbreviater</h5>
</footer>
</html>
''']

print(pagePiece[0], end='')

nextRep = 0
passCount = 0
removedCharCount = 0

for idx in range(len(inputText)):
    if passCount > 0:
        passCount -= 1
        continue

    if(idx == result[nextRep][0]):
        passCount = result[nextRep][1] - 1
        print('<font color="red">' + result[nextRep][2] + '</font>', end='')
        removedCharCount += result[nextRep][3];
        nextRep += 1
        continue

    print(inputText[idx], end='')

print(pagePiece[1], end='')

print(str(len(inputText)) + '자 중 ' + str(removedCharCount) + '자 축약됨', end='')

print(pagePiece[2], end='')
