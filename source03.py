import csv


sl = list()

with open("result.txt", "r") as file:
    text = file.readline()
    while text != "":
        s1 = text.split(",")
        d = dict()
        d[s1[0].split(" ")[0].split("'")[1]] = s1[0].split(" ")[1].split("'")[1]
        d[s1[1].split(" ")[1].split("'")[1]] = s1[1].split(" ")[2]
        d[s1[2].split(" ")[1].split("'")[1]] = s1[2].split(" ")[2]
        d[s1[3].split(" ")[1].split("'")[1]] = s1[3].split(" ")[2].split("}")[0]
        sl.append(d)
        text = file.readline()
    file.close()

with open("result.csv", "w") as csvfile:
    filednames = list(sl[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    for _, d in enumerate(sl):
        writer.writerow(d)
    csvfile.close()
