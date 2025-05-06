import pandas as pd
import pymysql


conn=pymysql.connect(
            host='localhost',
            user='root',
            password='9789472393',
            db='warehouse_db')

cursor=conn.cursor()
try:
    df=pd.read_excel('Consumables Report - Oct. 2022.xlsx',sheet_name='Kitchen - Oct 2022',usecols=[3],skiprows=4,nrows=142)
except Exception as e:
    print("Error reading Excel file:",e)
try:
    kitchen_data = df['Item List'].drop_duplicates()
    kitch_df=kitchen_data.to_frame(name='Item List')
    for _,row in kitch_df.iterrows():
        cursor.execute('INSERT IGNORE INTO kitchen(item_list) VALUES(%s)',(row['Item List'],))
    conn.commit()
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:",e)
