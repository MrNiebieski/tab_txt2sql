README.md
# tab_txt2sql
convert data in Excel to .sql file

This repo is intended to be used as a guideline rather than a completed build.

It does what it is intended to do.

    1.  Create a table in Excel and use the first line as header
    2.  Copy&Paste the table into a .txt file, it should be name as 
       <tablename>.txt; replace <tablename> with your table's name.
    3.  run this .py file, a GUI will pop up to prompt selection of the .txt
       file created in step 2, select it. Now a <tablename>.sql will be created
       with title <tablename>.sql, it is ready to be imported into SQL databases.

Note:
It may be necessary to add USE <databasename> before this .sql file.
