score = float(input("이번 외국어 영역의 백분위의 숫자만 입력해주세요. ex) 2.4"))

if score >100 or score <0:
    print("값을 이상하게 입력한것 같아요.")

if score >= 90 and score <= 100:
    print("A반으로 가세요.")

elif score >= 80 and score <= 90:
    print("B반으로 가세요.")

elif score >= 70 and score < 80:
    print("C반으로 가세요.")

elif score >= 60 and score < 70:
    print("D반으로 가세요.")

elif score < 60:
    print("E반으로 가세요.")


