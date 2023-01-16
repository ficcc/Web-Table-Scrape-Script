#Importing Pandas and fatetime
import pandas as pd 
from datetime import datetime

#Getting Time and Date 
dsyr = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

#Gettingn Url and Table no from User
url = input("Input Website  :   ")
tblno = input("Input Table no. (Starts with 0) :   ")

#Read Url and create a DataFrame
df = pd.read_html(url)
TableData = df[int(tblno)]
#Printing Dataframe into csv

TableData.to_csv(dsyr+' Data.csv')
print("Completed")
