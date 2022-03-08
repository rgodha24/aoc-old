# starting with input sorting

def oneListProcessing(file):
    temp = ""
    list = []
    for line in file:
        temp = line.strip()
        list.append(temp)

    return list