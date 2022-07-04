import sqlite3 as sq
 
import pandas as pd
   
class Create_DB():
    def DB_Creation(self):
        connection = sq.connect('Company_details.db')
 
        curs = connection.cursor()
 
        curs.execute("create table if not exists CompanyInfo" +
             " (SerialNumber integer,Name text, Address text, Ratings integer,Website text, Telephone text,YearsInBusiness text )")

        CompanyInfo = pd.read_csv('scrapped_data.csv')
 
        CompanyInfo.to_sql('CompanyInfo', connection, if_exists='replace', index=False)
        
        curs.execute('select * from CompanyInfo')
        
        records = curs.fetchall()
        
        for row in records:
            print(row)
            
        connection.close()

        