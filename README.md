# cron_parser
Parse the input cron job time to print all the time of the execution of the said job in a tabilar format.

Script is located in the folder 
venv > main_script.py


To execute the job
 - Open a terminal
 - python main_script.py "<d>"  // d > cron_string

for example: ` python script.py "*/15 0 1,15 * 1-5 /usr/bin/find" `
