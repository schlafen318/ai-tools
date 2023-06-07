import re

# Read csv file
with open('Success 2.0.txt', 'r') as file:
    lines = file.read()


# Remove everything in brackets
lines = re.sub(r'\[.*?\]', '', lines)

# Combine the lines into one
combined_line = lines.replace('\n', '')

# Write combined_line to 'transcript.txt' file
with open('transcript.txt', 'w') as file:
    file.write(combined_line)