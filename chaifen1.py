import pandas as pd
data = pd.read_excel(r"C:\Users\Baiye\Desktop\10月晋商对账\分地市\10月晋商拆分表.xlsx")
rows = data.shape[0]  #获取行数 shape[1]获取列数
department_list = []
 
for i in range(rows):
    temp = data["地市"][i]
    if temp not in department_list:
        department_list.append(temp)   #将地市的分类存在一个列表中
 
for department in department_list:
    new_df = pd.DataFrame()
 
    for i in range (0, rows):
        if data["地市"][i] == department:
            new_df = pd.concat([new_df, data.iloc[[i],:]], axis = 0, ignore_index = True)
    
    new_df.to_excel("10月合约惠对账单+"+str(department)+".xlsx", sheet_name="Sheet1", index = False)   #将每个地市存成一个新excel