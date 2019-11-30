# First usage
1. Visit https://console.cloud.google.com/ and create new project
2. Visit marketplace/library and enable google drive api
3. Create credentials (pick google drive api and web server) 
   then choose application data and click No, I'm not using them
4. Click What credentials do I need?
5. Pick your name and set role as project -> editor
6. Key type should be set as JSON
7. Enable google sheets api from library 
8. Clone this repository, create virtualenv and install requirements
9. Paste your downloaded credentials to main folder and rename it to credentials.json
10. Open credentials.json and copy your client_email
11. Now in your opened sheet click share and paste your client email


# Usage
12. In sheet.py change name to name of your sheet in sheet variable
13. Enable sheets.py script

# Additional notes
1. Remember, you have to set format type of two columns in your sheet: <br>
   - *Duration*
   - *Timestamps* - this one will be created after enable script (columns from **P7** to **P15**)
   
   *To change format type*: <br>
   1. Mark columns which you want to change
   2. Click *format* from top menu
   3. Hover on *Number*
   4. Choose *Duration* from bottom of list


