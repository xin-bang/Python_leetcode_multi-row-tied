#!usr/bin/python 

import pandas as pd

df = pd.read_excel("test2.xlsx",sheet_name="Sheet1")
index = ["sample","原始数据量","样品浓度","质控合格比例","Q30","质控情况","patho_namezn","建库方式","patho_RPK","filter_flag"]
df = df[index]
df['newindex'] = df['sample'].apply(lambda x: x.strip().split("-")[-1])
# df = df[df['patho_namezn'] != "/"]

df = df.drop_duplicates()
# df.to_excel("test11.xlsx")


new_df = pd.DataFrame()
# new_df = pd.DataFrame()
multi_index = pd.MultiIndex.from_tuples([], names=['patho_namezn', 'newindex'])
new_df.set_index(multi_index, inplace=True)
for item in df['newindex'].unique().tolist():
    
    df_1 = df.loc[df["newindex"]== item,].copy()

    # sample1 = df_1.loc[df_1['sample'] == "T2P2-A-ZDH-" + item,].copy() 
    sample1 = df_1.loc[df_1['sample'] == "T2P2-A-ZDH-" + item,].copy() 
    sample2 = df_1.loc[df_1['sample'] == "T2P2-B-ZDH-" + item,].copy()   #T2P2-SD-56
    sample3 = df_1.loc[df_1['sample'] == "T2P2-SD-" + item,].copy()
    index2 = ["sample","原始数据量","样品浓度","质控合格比例","Q30","质控情况","建库方式","filter_flag",'patho_namezn']
    # sample1_A= sample1[index2].drop_duplicates()
    # sample2_A= sample2[index2].drop_duplicates()
    sample1_2= sample1[index2].drop_duplicates()
    sample2_2= sample2[index2].drop_duplicates()
    sample3_2= sample3[index2].drop_duplicates()

    for patho in df_1['patho_namezn'].unique().tolist():
        df_2 = df_1.loc[df_1['patho_namezn'] == patho,].copy()

        sample1_A = sample1_2.loc[sample1_2['patho_namezn'] == patho,].copy()
        sample2_A = sample2_2.loc[sample2_2['patho_namezn'] == patho,].copy()
        sample3_A = sample3_2.loc[sample3_2['patho_namezn'] == patho,].copy()



        new_df.at[(patho, item),"sample_A"] = sample1_2['sample'].iloc[0]
        new_df.at[(patho, item),"原始数据量_A"] = sample1_2['原始数据量'].iloc[0]
        new_df.at[(patho, item),"样品浓度_A"] = sample1_2['样品浓度'].iloc[0]
        new_df.at[(patho, item),"质控合格比例_A"] = sample1_2['质控合格比例'].iloc[0]
        new_df.at[(patho, item),"Q30_A"] = sample1_2['Q30'].iloc[0]
        new_df.at[(patho, item),"质控情况_A"] = sample1_2['质控情况'].iloc[0]
        new_df.at[(patho, item),"建库方式_A"] = sample1_2['建库方式'].iloc[0]
        

        try:
            new_df.at[(patho, item),"filter_flag_A"] = sample1_A['filter_flag'].iloc[0]
        except IndexError:
            new_df.at[(patho, item),"filter_flag_A"] = "/"   ###这里出问题了，原来是filter_flag_B
            # print("fuck")
        # filter_flag
        try:
            new_df.at[(patho, item),"RPK_A"] = sample1.loc[sample1['patho_namezn']==patho,]['patho_RPK'].iloc[0]
        except IndexError:
            new_df.at[(patho, item),"RPK_A"] = 0





        new_df.at[(patho, item),"sample_B"] = sample2_2['sample'].iloc[0]
        new_df.at[(patho, item),"原始数据量_B"] = sample2_2['原始数据量'].iloc[0]
        new_df.at[(patho, item),"样品浓度_B"] = sample2_2['样品浓度'].iloc[0]
        new_df.at[(patho, item),"质控合格比例_B"] = sample2_2['质控合格比例'].iloc[0]
        new_df.at[(patho, item),"Q30_B"] = sample2_2['Q30'].iloc[0]
        new_df.at[(patho, item),"质控情况_B"] = sample2_2['质控情况'].iloc[0]
        new_df.at[(patho, item),"建库方式_B"] = sample2_2['建库方式'].iloc[0]

        try:
            new_df.at[(patho, item),"filter_flag_B"] = sample2_A['filter_flag'].iloc[0]     ###这里有问题：列表中的第一个？
            
        except IndexError:
            new_df.at[(patho, item),"filter_flag_B"] = "/"
        try:
            new_df.at[(patho, item),"RPK_B"] = sample2.loc[sample2['patho_namezn']==patho,]['patho_RPK'].iloc[0]
        except IndexError:
            new_df.at[(patho, item),"RPK_B"] = 0



        new_df.at[(patho, item),"sample_C"] = sample3_2['sample'].iloc[0]
        new_df.at[(patho, item),"原始数据量_C"] = sample3_2['原始数据量'].iloc[0]
        new_df.at[(patho, item),"样品浓度_C"] = sample3_2['样品浓度'].iloc[0]
        new_df.at[(patho, item),"质控合格比例_C"] = sample3_2['质控合格比例'].iloc[0]
        new_df.at[(patho, item),"Q30_C"] = sample3_2['Q30'].iloc[0]
        new_df.at[(patho, item),"质控情况_C"] = sample3_2['质控情况'].iloc[0]
        new_df.at[(patho, item),"建库方式_C"] = sample3_2['建库方式'].iloc[0]

        try:
            new_df.at[(patho, item),"filter_flag_C"] = sample3_A['filter_flag'].iloc[0]     ###这里有问题：列表中的第一个？
            # print (sample3_A)
        except IndexError:
            new_df.at[(patho, item),"filter_flag_C"] = "/"
        try:
            new_df.at[(patho, item),"RPK_C"] = sample3.loc[sample3['patho_namezn']==patho,]['patho_RPK'].iloc[0]
        except IndexError:
            new_df.at[(patho, item),"RPK_C"] = 0

        # if item == "75" and patho == "大肠埃希菌":
        #     print('hi')
        # else:
        #     pass

new_df.to_excel("test33_2.xlsx")








# pivoted = df.pivot_table(index=['newindex'], columns='建库方式', values=['原始数据量', '样品浓度',"质控合格比例","Q30",])
# pivoted.reset_index(inplace=True)
# pivoted.columns = pivoted.columns.map('_'.join).str.rstrip('_')

print ("hi")

















# data = {'sample': ['A-1', 'B-1'],
#         '样品浓度_自动': [36.63, 37.63],
#         '质控合格比例_自动': [0.848, 1.848],
#         'patho': ['疯牛', '新城疫'],
#         'RPK': [1, 2]}

# df = pd.DataFrame(data)
# df['newindex'] = df['sample'].apply(lambda x:x.strip().split("-")[-1])
# # 使用melt函数将数据从宽格式转换为长格式
# melted = pd.melt(df, id_vars=['sample', 'newindex'], var_name='测量项')

# print ("hi")