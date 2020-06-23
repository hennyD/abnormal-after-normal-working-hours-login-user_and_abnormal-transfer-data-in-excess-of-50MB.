# abnormal_login_user-and-abnormal-transfer-data-in-excess-of-50MB-after-normal-working-hours

extract_abnormal_login_time.py - Write a script to search an audit log or access control system log in to identify system users who repeatedly log-on after normal local business hours.
extract_abnormal_login_time_and_filesize_exceed.py - Write a script to search and audit log or access control system log to identify system users who repeatedly transfer data in excess of 50MB after normal working hours. 
Usage: 
1.	python extract_abnormal_login_time.py  ${fileRootName} ------This will generate a file called abnormal_time_login.txt, will extract records of users who repeatedly log-on after normal local business hours of all logs in the folder fileRootName into this file


2.	python extract_abnormal_login_time_and_filesize_exceed  ${fileRootName} ------ Similar like above, in abnormal_time_login_exceed_file_size.txt

If you want a schedule, for Linux server, use 
crontab -e  then insert:
00 00 * * * python extract_abnormal_login_time.py  ${fileRootName}
00 00 * * * python extract_abnormal_login_time_and_filesize_exceed  ${fileRootName} 

This will excute the scripts every day at 00:00
