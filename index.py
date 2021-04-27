#!/usr/bin/python3
print("Content-Type: text/html; charset=utf-8")
print()
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("""
<!DOCTYPE html>
<html>
<head>
	<title>글자수 축약기</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
	<h1 align="center">글자수 축약기</h1>
	<h3 align="center">글자수를 줄일 텍스트를 입력해주세요.</h3>
	<h6 id="protect-information" align="center">*본 서비스는 사용자의 사용 정보를 일체 저장하지 않으며 서비스 제공 목적으로 수집된 정보는 서비스 제공 이후 즉시 파기됩니다.</h6>
	<div class="list-container" align="center">
		<form method="post" action="analysis.py" id="form-container">
	  		<input type="textarea" class="centered-item" id="text-box" name="inputText"/>
			<input class="centered-item" class="button1" id="submit-button" name="submit" type="submit" value="분석"/>
		</form>
	</div>
</body>
<footer>
	<h5 align="center" id="madeby-information">made by CaChiJ</h5>
	<h5 align="center" id="contact-information">contact : chj7239@gmail.com | https://github.com/CaChiJ/Abbreviater</h5>
</footer>
</html>
""")
