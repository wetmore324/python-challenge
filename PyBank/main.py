import os
import csv

#Reading csv with csv module
CSV_PATH= os.path.join('Resources', 'budget_data.csv')


MONTH_IDX = 0
PROFIT_IDX = 1


month_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header:{csv_header}")
    
    for row in csvreader:
        month_count += 1
        current_month = row[MONTH_IDX]
        current_profit = int(row[PROFIT_IDX])
        total_profit = current_profit[]
        print(current_month, current_profit, type(current_profit))
    print(month_count, total_profit)
    

        

