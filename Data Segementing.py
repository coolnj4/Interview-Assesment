from datetime import datetime

with open('data.xyz', 'r') as file:
    file_content = file.readlines()

segment_1_end = '18:51:35.232'
segment_2_end = '19:02:14.621'

def timestamp_to_datetime_object(time_str):
    return datetime.strptime(time_str, '%H:%M:%S.%f')

segment_1_end_time = timestamp_to_datetime_object(segment_1_end)
segment_2_end_time = timestamp_to_datetime_object(segment_2_end)

segment_1 = []
segment_2 = []
segment_3 = []

for line in file_content:
    parts = line.split()  
    time_str = parts[1]

    timestamp = timestamp_to_datetime_object(time_str)

    if timestamp <= segment_1_end_time:
        segment_1.append(line)
    elif segment_1_end_time < timestamp <= segment_2_end_time:
        segment_2.append(line)
    else:
        segment_3.append(line)

print(len(segment_1), len(segment_2), len(segment_3))

with open('segment_1', 'w') as file:
    file.writelines(segment_1)

with open('segment_2', 'w') as file:
    file.writelines(segment_2)

with open('segment_3', 'w') as file:
    file.writelines(segment_3)

