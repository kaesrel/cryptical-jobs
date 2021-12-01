import csv


file_out = open("crypto_info.csv", 'w')


with open("world_crypto_pop.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        country = row[0]
        population = row[1].replace(',','')
        output = f'{country},"{population}"\n'
        file_out.write(output)




