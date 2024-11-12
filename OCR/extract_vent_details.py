import re
from extract_text_from_image import extracted_text

def extract_event_details(extracted_text):

    event_pattern = re.compile(r"(Day \d.*?:\s?.*)")  # Matches event titles like "Day 1: Haldi Ceremony"
    date_pattern = re.compile(r"Date:\s*(.*)")  # Matches "Date: March 15, 2023"
    time_pattern = re.compile(r"Time:\s*(.*)")  # Matches "Time: 10:00 AM"
    location_pattern = re.compile(r"Location:\s*(.*)")  # Matches "Location: Family Residence"

    events = []


    event_titles = event_pattern.findall(extracted_text)
    dates = date_pattern.findall(extracted_text)
    times = time_pattern.findall(extracted_text)
    locations = location_pattern.findall(extracted_text)


    for i in range(len(event_titles)):
        event = {
            'title': event_titles[i],
            'date': dates[i] if i < len(dates) else "N/A",
            'time': times[i] if i < len(times) else "N/A",
            'location': locations[i] if i < len(locations) else "N/A"
        }
        events.append(event)
    
    return events


events = extract_event_details(extracted_text)


print("Extracted Event Details:\n")
for event in events:
    print(event)
