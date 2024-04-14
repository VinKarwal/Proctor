# import csv
# from itertools import product
# import pandas as pd
# from collections import defaultdict

# # Read data from CSV file
# data = []
# with open('Test.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         data.append(row)

# # Define available lab numbers, time slots, and dates
# examiners = ['Dr. Alankrita Agrawal', 'Dr. Anita Sardana', 'Mr Jagjeet Singh', 'Mr. Mohit Lalit', 'Ms. Shaveta Jain', 'Mr. Aadi Pratap', 'Dr. Deepak Kumar', 'Dr. Madan Lal', 'Dr. Kalpana Singh', 'Mr. Mukesh Birla', 'Dr. Mahadev', 'Dr. Rajat Tiwari', 'Dr. Ratish Kumar', 'Dr. Shikha Gupta', 'Mr. Kushagra Agrawal', 'Dr. U. Hariharan', 'Dr. Vineet Mehan', 'Mr. Arun Mittal', 'Mr. Bharat Tripathi', 'Mr. Dayal Chand', 'Dr. Sudhanshu', 'Mr. Mohit lalit', 'Mr. Saurabh Singhal', 'Ms. Shubhangi Mishra', 'Mr. Nirmalya Basu', 'Mr. Sant Maurya', 'Mr. Sashi Tarun', 'Mr. Shubham Khari', 'Mr. Sumit Kharra', 'Ms. Amanpreet Kaur', 'Ms. Deeksha', 'Ms. Harshleen Kaur', 'Ms. Kangan Arora', 'Mr. Vikash Kumar:E13657', 'Ms. Sonal Rattan', 'Ms.Ramneet Kaur(E13422)', 'Ms. Neha Sharma', 'Ms. Ravneet Kaur', 'Dr Prasenjit Das', 'Mr Abhinav Raghav', 'Dr. Gurwinder Singh', 'Mr. Ankur Sharma', 'Dr. Binayak Dutta', 'Mrs. Somdatta Patra', 'Ms.Samriti: E13663', 'Mr. Vikash Kumar: E13657', 'Mrs. Neeru Bala', 'Mr. Parkash Mani Badal', 'Ms.Aanchal Sharma:E13879', 'Mr. Swapnil Raj', 'Mr. Abhishek Ankur', 'Mr. Vishal Kumar Kanaujia', 'Mr. Anil Manohar Dogra', 'Mr. Nikhil Aggarwal', 'Dr. Ankur Thakur', 'Mr. Harun (E11421)', 'Ms. Sukhmeet Kaur (E13420)', 'Dr. Geeta Arora', 'Ms Aanchal Sharma:E13879', 'Dr. Prasenjit Das', 'Mr. Yogiraj Anil Bhale', 'Dr.Maram Balajee:E15007', 'Ms. Yashika Sharma', 'Mr. Aman Kaushik', 'Mr Chandra Bhan Singh', 'Mr Ankur Sharma', 'Ms. Manisha (E11606)', 'Mr. Pramod Vishwakarma', 'Ramneet Kaur:E13422', 'Chandra Bhan Singh:E11667']
# lab_numbers = ['D2-411', 'D2-307', 'D2-308', 'D2-415', 'D2-409', 'D2-306', 'D3-209', 'D2-317', 'D2-318', 'D2-512', 'D4-104', 'D2-408', 'D3-209A', 'D2-410', 'D2-514', 'D2-513', 'D4-106', 'D2-416', 'D2-414', 'D2-413', 'D2-508', 'D3-209-A', 'D2-207', 'D2-412', 'D4-103', 'D3-101', 'D3-210']
# time_slots = ['9:30 AM - 11:10 AM', '11:10 AM - 12:50 PM', '1:00 PM - 2:40 PM', '2:40 PM - 4:20 PM']
# dates = ['2024-03-28', '2024-03-29', '2024-03-30']

# # Dictionary to keep track of assigned time slots for each section and group combination
# section_group_time_slots = defaultdict(lambda: defaultdict(list))

# # Function to check for conflicts
# def check_conflict(row, lab_number, time_slot, date, examiner):
#     section_and_group = (row.get('Class with Section'), row.get('Group (A,B)'))

#     # Check if the examiner conflicts with the Internal Examiner of the same row
#     if row.get('Internal Examiner') == examiner:
#         return True

#     # Check if the examiner already has a duty at the same time slot and date
#     for other_row in data:
#         if (
#             other_row.get('Examiner') == examiner
#             and other_row.get('Time Slot') == time_slot
#             and other_row.get('Date') == date
#         ):
#             return True

#     # Check if the lab number, time slot, and date are already assigned to another row
#     for other_row in data:
#         if (
#             other_row.get('Lab Number') == lab_number
#             and other_row.get('Time Slot') == time_slot
#             and other_row.get('Date') == date
#         ):
#             return True

#     # Check if the section and group combination already has two time slots assigned for the same date
#     if len(section_group_time_slots[section_and_group][date]) >= 2:
#         return True

#     return False

# # Assign lab numbers, time slots, dates, and examiners
# for row in data:
#     for lab_number, time_slot, date, examiner in product(lab_numbers, time_slots, dates, examiners):
#         if not check_conflict(row, lab_number, time_slot, date, examiner):
#             row['Lab Number'] = lab_number
#             row['Time Slot'] = time_slot
#             row['Date'] = date
#             row['Examiner'] = examiner
#             section_and_group = (row.get('Class with Section'), row.get('Group (A,B)'))
#             section_group_time_slots[section_and_group][date].append(time_slot)
#             break

# # Save the updated data to a new CSV file
# fieldnames = data[0].keys()
# with open('Test_updated.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)

# df = pd.DataFrame(data)
# # Save the updated data to a new xlsx file
# df.to_excel('Test_updated.xlsx', index=False)


# v.2
import csv
from itertools import product
import pandas as pd
from collections import defaultdict

data = []
with open('backend/data/input/class.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

examiners = ['ANKUR GUPTA', 'Ms. Rubbina', 'Ms. Geetanjali Pandey', 'Dr. Ankit Garg', 'Shubham Banik', 'Ms. Pavandeep Kaur', 'Dr. Dhawan Singh', 'Ms. Bhavna Nayyar', 'Dr. Monika Singh', 'Dr. Deepti Sharma', 'Dr. Ranjan Walia']
lab_numbers = ['D2-207', 'D2-306', 'D2-307', 'D2-308', 'D2-317', 'D2-318', 'D2-408', 'D2-409', 'D2-410', 'D2-411', 'D2-412', 'D2-413', 'D2-414', 'D2-415', 'D2-416', 'D2-508', 'D2-512', 'D2-513', 'D2-514', 'D3-101', 'D3-209-A', 'D3-209', 'D3-210', 'D3-211', 'D4-101', 'D4-102', 'D4-103', 'D4-104', 'D4-106']
time_slots = ['9:30 AM - 11:00 AM', '11:15 AM - 12:45 PM', '1:15 PM - 2:45 PM', '3:00 PM - 4:30 PM']
dates = ['2024-04-25', '2024-04-26', '2024-04-27', '2024-04-29']

section_group_time_slots = defaultdict(lambda: defaultdict(list))
examiner_time_slots = defaultdict(lambda: defaultdict(list))

def check_conflict(row, lab_number, time_slot, date, examiner, force=False):
    section_and_group = (row.get('Class with Section'), row.get('Group (A,B,C,D)'))

    if row.get('Internal Examiner') == examiner:
        return True

    if len(examiner_time_slots[examiner][date]) >= 2:
        return True

    time_slot_index = time_slots.index(time_slot)
    if (
        (time_slot_index > 0 and time_slots[time_slot_index - 1] in examiner_time_slots[examiner][date])
        or (time_slot_index < len(time_slots) - 1 and time_slots[time_slot_index + 1] in examiner_time_slots[examiner][date])
    ):
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

for row in data:
    for lab_number, time_slot, date, examiner in product(lab_numbers, time_slots, dates, examiners):
        if not check_conflict(row, lab_number, time_slot, date, examiner):
            row['Lab Number'] = lab_number
            row['Time Slot'] = time_slot
            row['Date'] = date
            row['External Examiner'] = examiner
            section_and_group = (row.get('Class with Section'), row.get('Group (A,B)'))
            section_group_time_slots[section_and_group][date].append(time_slot)
            examiner_time_slots[examiner][date].append(time_slot)
            break

fieldnames = data[0].keys()
with open('backend/data/output/output.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

df = pd.DataFrame(data)
df.to_excel('backend/data/output/output.xlsx', index=False)