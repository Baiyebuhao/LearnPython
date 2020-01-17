height = float(input('请输入身高'))
weight = float(input('请输入体重'))

bmi=float(weight/float((height*height)))
if  bmi<18.5:
    print('过轻')
elif bmi>=18.5 and bmi<=25:
    print('正常')
elif  bmi>=25 and bmi<=28:
    print('过重')
else  :
    print('严重肥胖')