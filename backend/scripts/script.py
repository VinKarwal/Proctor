import csv
from itertools import product
import pandas as pd
from collections import defaultdict

xls = pd.ExcelFile('backend/data/input/ClassList.xlsx')

# Get the names of all worksheets in the Excel file
sheet_names = xls.sheet_names

# Exclude the 'Faculty details' worksheet
sheet_names.remove('Faculty details')

# Initialize an empty list to store the data from all worksheets
all_data = []

# Loop through each worksheet
for sheet_name in sheet_names:
    # Read the worksheet into a DataFrame
    df = pd.read_excel(xls, sheet_name)

    # Standardize the column names
    df.columns = ['Sr No', 'Branch', 'Semester', 'Subject Name', 'Subject Code', 'Class with Section', 'Group', 'Total Students', 'Internal Examiner', 'EMP Code']

    # Convert the DataFrame to a list of dictionaries
    data_list = df.to_dict('records')

    # Append the data list to all_data, excluding rows where 'Sr No' is 'Sr No'
    all_data.extend([row for row in data_list if row['Sr No'] != 'Sr No'])
    
# Now all_data contains data from all worksheets
data = all_data
        
lab_data = pd.read_excel('backend/data/input/labList.xlsx')

# Fetch the lab numbers
lab_numbers = lab_data['Lab No'].tolist()
examiners = list(set(row['Internal Examiner'] for row in data))
time_slots = ['9:30 AM - 11:00 AM', '11:15 AM - 12:45 PM', '1:15 PM - 2:45 PM', '3:00 PM - 4:30 PM']
dates = ['2024-04-25', '2024-04-26', '2024-04-27', '2024-04-29']

section_group_time_slots = defaultdict(lambda: defaultdict(list))
examiner_time_slots = defaultdict(lambda: defaultdict(list))

lab_info = lab_data[['Lab No', 'Capacity']].to_dict('records')
lab_capacity = {lab['Lab No']: lab['Capacity'] for lab in lab_info}

def check_conflict(row, lab_number, time_slot, date, examiner, force=False):
    section_and_group = (row.get('Class with Section'), row.get('Group (A,B,C,D)'))

    # Check if the lab has the capacity to handle the class
    if row['Total Students'] > lab_capacity[lab_number]:
        return True
    
    # Check if the examiner is already assigned as an internal or external examiner at the same time slot and date
    for other_row in data:
        if (
            (other_row.get('Internal Examiner') == examiner or other_row.get('External Examiner') == examiner)
            and other_row.get('Time Slot') == time_slot
            and other_row.get('Date') == date
        ):
            return True

    if time_slot in examiner_time_slots[examiner][date]:
        return True

    if len(examiner_time_slots[examiner][date]) >= 3:
        return True

    time_slot_index = time_slots.index(time_slot)
    if (
        (time_slot_index > 0 and time_slots[time_slot_index - 1] in examiner_time_slots[examiner][date])
        or (time_slot_index < len(time_slots) - 1 and time_slots[time_slot_index + 1] in examiner_time_slots[examiner][date])
    ):
        return True

    if len(examiner_time_slots[examiner][date]) == 2:
        if sorted(examiner_time_slots[examiner][date]) not in [['9:30 AM - 11:00 AM', '11:15 AM - 12:45 PM', '3:00 PM - 4:30 PM'], ['9:30 AM - 11:00 AM', '1:15 PM - 2:45 PM', '3:00 PM - 4:30 PM']]:
            return True

    for other_row in data:
        if (
            other_row.get('Lab Number') == lab_number
            and other_row.get('Time Slot') == time_slot
            and other_row.get('Date') == date
        ):
            return True

    if force and len(section_group_time_slots[section_and_group][date]) >= 2:
        return True
    return False


def get_least_busy_examiner():
    return min(examiners, key=lambda examiner: examiner_duties[examiner])

examiner_duties = defaultdict(int)
# Sort the data by 'Total Students' in descending order before assigning labs
data.sort(key=lambda row: row['Total Students'], reverse=True)

for row in data:
    examiner_duties[row['Internal Examiner']] += 1
    for lab_number, time_slot, date in product(lab_numbers, time_slots, dates):
        examiner = get_least_busy_examiner()
        if not check_conflict(row, lab_number, time_slot, date, examiner):
            row['Lab Number'] = lab_number
            row['Time Slot'] = time_slot
            row['Date'] = date
            row['External Examiner'] = examiner
            row['Lab Capacity'] = lab_capacity[lab_number] 
            section_and_group = (row.get('Class with Section'), row.get('Group (A,B,C,D)'))
            section_group_time_slots[section_and_group][date].append(time_slot)
            examiner_time_slots[examiner][date].append(time_slot)
            examiner_duties[examiner] += 1
            break

# Print the number of duties each teacher is getting as an internal and external examiner
for examiner in examiners:
    print(f'{examiner}\t-> Total: {examiner_duties[examiner]}')

# sort it back into sr. no as well
data.sort(key=lambda row: row['Sr No'])

fieldnames = data[0].keys()
with open('backend/data/output/output1.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

df = pd.DataFrame(data)
df.to_excel('backend/data/output/output1.xlsx', index=False)

# Class Path: backend\data\input\ClassList.xlsx
# Lab Path: backend\data\input\LabList.xlsx
# time_slots = ['9:30 AM - 11:00 AM', '11:15 AM - 12:45 PM', '1:15 PM - 2:45 PM', '3:00 PM - 4:30 PM']
# dates = ['2024-04-25', '2024-04-26', '2024-04-27', '2024-04-29']
