# GNB - 1st - Reading Files Notes
import csv

while True:
    try:
        with open("notes/reading_files_notes/reading.txt", "r") as file: #As you can see, it is 67 or wtv
            for line in file:
                print(f"Welcome to {line.strip()}")
           # content = file.read()
          #  print(content)
    except:
        print("That file can't be found...")
    else:
        print("Good night everyone")
        break


try:
    with open("notes/reading_files_notes/sample_fr.csv", mode = "r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        rows = []
        for line in content:
            #print(f"{line[0]}: {line[1]}")
            rows.append({headers[0]: line[0], headers[1]: line[1]})

except:
    print("File couldn't be found")
else:
    for line in rows:
        print(line)