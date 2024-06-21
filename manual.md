# How To Use

1. Get .csv from Wallet of Satoshi
2. Name it "censored.csv"
3. Define file_path as 'censored.csv'
4. Define `start_date`
5. Execute cal.py to generate sales_report.md
6. Edit each JPY column
7. Execute recal.py to sum JPY on sales_report.md
8. Execute updateusdt.py to add USDT column on sales_repodt.md
9. Execute `pandoc sales_report.md -o 20xx-x-x-sales-report.pdf -t latex --pdf-engine=/Library/TeX/texbin/pdflatex`
