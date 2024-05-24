# How To Use

1. Get .csv from Wallet of Satoshi
2. Name it "censored.csv"
3. Define file_path as 'censored.csv'
4. Define `start_date`
5. Execute cal.py to generate sales_report.md
6. Edit each JPY column
7. Execute recal.py to sum JPY on sales_report.md
8. Execute `pandoc -f markdown -t pdf -o 20xx-x-x-sales-report.pdf sales_report.md`
