import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(credentials)

# You have to change this name to your sheet name
sheet = client.open("your_sheet_name").sheet1

tags = sheet.col_values(13)

tags.remove('Tags')
unique_tags = list(dict.fromkeys(tags))


START_INDEX = 7
sheet.update_cell(6, 15, "SUM")
for tag in unique_tags:
    sheet.update_cell(START_INDEX, 15, tag)
    sheet.update_cell(START_INDEX, 16, "=SUMIF(M2:M; " + '"' + tag + '"' + "; L2:L)")
    START_INDEX += 1

sheet.update_cell(6, 16, "=SUM(P7:P15)")
