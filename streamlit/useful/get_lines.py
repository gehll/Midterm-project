
# Function to get unique lines in selected transport types

def get_lines(data):
    lines = []
    for transportType in data:
        for doc in transportType:
            if isinstance(doc['Lines'], list):
                for line in doc:
                    if line not in lines:
                        lines.append(line)
            else:
                if doc['Lines'] not in lines:
                    lines.append(doc['Lines'])

    return lines
