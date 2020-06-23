
import os
import sys
import time

unusual_log=[]
unusual_log_file_size=[]

business_begin_time = '06:00'
business_end_time = '20:00'
dest_log_repeat_logon_after_normal_time="abnormal_time_login.txt"


def extract_abnormal_log(source_log_name,file_root):
    f2 = open(source_log_name, "r")
    lines = f2.readlines()
    for line in lines:
        try:
            item = line.split(" ")
            time = item[4]
            file_size = item[5]
        except:
            continue
        if not business_begin_time <= time <= business_end_time:
            unusual_log.append(line)
        if (not business_begin_time <= time <= business_end_time) and float(file_size) > 50:
            unusual_log_file_size.append(line)

    values1 = ''.join(str(v) for v in unusual_log)

    fh = open(file_root+"/"+dest_log_repeat_logon_after_normal_time, 'w')
    fh.write(values1+"\n")
    fh.close()


def start(file_root):
    for maindir, subdir, file_name_list in os.walk(file_root):
            for filename in file_name_list:
                path = os.path.join(maindir, filename)
                if filename.endswith(".log"):
                    extract_abnormal_log(path, file_root)


if __name__ == '__main__':
    start(sys.argv[1])
    print("extracted abnormal log of users who repeatedly log-on after normal local business hours")
        
