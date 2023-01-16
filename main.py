import pandas as pd
import gspread
import inputs as inp


#print(url)
#df = pd.read_csv(url)
#print(df)

#Write a spreadsheet 
gc = gspread.service_account()
spreadsheet = gc.open_by_key(inp.SHEET_ID)
worksheet = spreadsheet.worksheet(inp.SHEET_NAME)

rows = worksheet.get_all_records()
#print(rows[:5])

#print('==============================')
#df = pd.DataFrame(rows)
#print(df)

worksheet.update('A4:D4', [['01/05/2003', '17:00', 20,'NO']])