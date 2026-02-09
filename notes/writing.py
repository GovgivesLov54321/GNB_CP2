# GNB - 1st - Writing To Notes

import csv 

with open("notes/reading_files_notes/reading.txt", "w") as file: #w for write
    file.write("I wrote on my file... :O")

print("Code end")

with open("notes/writing.txt", "a") as file: # a for append/add -- 
    file.write("\nThis is more on my file...")

print("code end")

#with open("notes/reading_files_notes/proof.txt", "r+") as file: #w for write
  #  content = file.read()
  #  content += "\nI wanna be 6'7 fr..."
  #  file.write(content)

#print("Code end")


with open("notes/reading_files_notes/sample_fr.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",") # delimiter is what seperates each character
    writer.writerow(["username", "Orange"])

print("Code is done")

with open("notes/sample_new.csv", "r+", newline="") as csvfile:
    fieldnames = ['username', 'colore']
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # delimiter is what seperates each character
    #writer.writeheader()
    writer.writerow({"username": "Mister 67", "color": "Orange"})
    writer.writerow({"username": "Mister 89", "color": "Yellow"})
    writer.writerow({"username": "Mister 1011", "color": "Green"})
    writer.writerow({"username": "Mister 1213", "color": "Blue"})
    writer.writerow({"username": "Mister 41", "color": "Violet"})

print("Code is done")