import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(credentials)

try:
    sheet = client.open(sys.argv[1]).sheet1
except (gspread.SpreadsheetNotFound, IndexError):
    print("Spreadsheet not found")
    sys.exit()

try:
    tags = sheet.col_values(13)
    tags.remove('Tags')
    unique_tags = list(dict.fromkeys(tags))
except ValueError:
    print("Your spreadsheet cannot be modified and should contain original columns from toggle reports.")
    sys.exit()


START_INDEX = 7
sheet.update_cell(6, 15, "SUM2")
for tag in unique_tags:
    sheet.update_cell(START_INDEX, 15, tag)
    sheet.update_cell(START_INDEX, 16, "=SUMIF(M2:M; " + '"' + tag + '"' + "; L2:L)")
    START_INDEX += 1

sheet.update_cell(6, 16, "=SUM(P7:P15)")
