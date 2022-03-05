import csv
with open('text.txt',mode='w') as outf:
    fieldnames=['Name','Department','BirthDay Month']
    content=csv.DictWriter(outf,fieldnames=fieldnames)
    content.writeheader()
    content.writerow({'Name':'John','Department': 'Accounting','BirthDay Month': 'November'})
    content.writerow({'Name': 'Amy','Department':'IT','BirthDay Month':'March'})