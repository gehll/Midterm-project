
# Function to get unique lines in selected transport types

def get_lines(data: list):
    '''
    This function receives a list of 1 or more lists that contain different types of public transport stations in Barcelona.
    The function returns all unique lines for each type of transport
    '''
    lines = []
    for transportType in data:  # "data" is a list of 1 or more lists with each type of transport station in Barcelona
        for doc in transportType:  # Each type of transport contains JSON-style objects with the data
            if isinstance(doc['Lines'], list):  # "Lines" can come in lists or as a string
                for line in doc['Lines']:
                    if line not in lines:
                        lines.append(line)
            else:
                if doc['Lines'] not in lines:
                    lines.append(doc['Lines'])

    return lines
