import os
import yaml
import pandas as pd
folder_path = r"D:\stock_project\yaml_files"
all_data=[]
for file in os.listdir(folder_path):
    if file.endswith(".yaml"):
        file_path = os.path.join(folder_path,file)
        with open(file_path,"r") as f:
            data = yaml.safe_load(f)
        df=pd.DataFrame(data)
        all_data.append(df)
df1=pd.concat(all_data,ignore_index=True)
print(df1.shape) 
print(df1.dtypes) 

# Data Cleaning
df1["date"] = pd.to_datetime(df1["date"], errors="coerce")
print(df1["date"].dtype) 
output_folder = r"D:\stock_project\ticker_csvs"
os.makedirs(output_folder, exist_ok=True)

for ticker in df1["Ticker"].unique():
    ticker_df = df1[df1["Ticker"] == ticker]
    ticker_df.to_csv(os.path.join(output_folder, f"{ticker}.csv"),index=False)

print("CSV files created successfully")    
