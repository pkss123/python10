ssn = input("주민번호를 입력하세요: ")
birth = ssn[0:2]
if (int(ssn[7]) % 2 == 1):
    gender = "남자"
else:
    gender = "여자"
print("%s년생 %s" % (birth, gender))