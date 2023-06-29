# cron_parser
Parse the input cron job time to print all the time of the execution of the said job in a tabular format.

A schedule is defined using the unix-cron string format (* * * * *) which is a set of five fields in a line, indicating when the job should be executed.

![image](https://github.com/avj13/cron_parser/assets/49868709/42e4edeb-8f0d-4ab8-8750-28c4c65b8c96)


Script is located in the folder 
venv > main_script.py


To execute the job
 - Open a terminal
 - python main_script.py "<d>"  // d > cron_string

for example: ` python script.py "*/15 0 1,15 * 1-5 /usr/bin/find" `

Expected output in the format:

![image](https://github.com/avj13/cron_parser/assets/49868709/02e10e49-febb-4a86-9152-c6eb6dab140b)

