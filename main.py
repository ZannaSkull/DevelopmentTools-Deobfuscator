# import base64, codecs, and sys
import base64
import codecs
import sys

# Check for user parameter without flag for file input, check for output flag and set output destination
if sys.argv[1] == "-o":
    output = sys.argv[2]
    input = sys.argv[3]
else:
    input = sys.argv[1]

# Open file and read contents
with open(input, "r") as f:
    data = f.read().split('\n')

# For each line, check for '=', and execute
for line in data:
    if '=' in line:
        exec(line)

deobfusCode = base64.b64decode(eval('trust')).decode()

# If output flag is set, write to file, else print to console
if sys.argv[1] == "-o":
    with open(output, "w") as f:
        f.write(deobfusCode)
else:
    print(deobfusCode)