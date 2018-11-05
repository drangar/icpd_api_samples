import pandas as pd

sales_person = pd.read_csv("person.csv",names=["PID","PERSON_NAME"],header=0,sep="|")
aggregated_sales = pd.read_csv("intermediate_results.csv",names=["PID","SALES_AMT"],header=0,sep="\t")

merged = sales_person.merge(aggregated_sales, on='PID', how='inner')
merged.to_csv("final.csv")
