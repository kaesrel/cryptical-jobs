from array import array
from my_resource import *
import random


NUMBER_OF_PEOPLE = 1000


file_person = open("data.sql", 'w')


country = random.choices(countries, weights=country_wgts, k=NUMBER_OF_PEOPLE)
job = random.choices(list(dict_jobs), weights=job_wgts, k=NUMBER_OF_PEOPLE)
prefer_crypto = random.choices(cryptocurrencies, weights=crypto_prefer_wgts, k=NUMBER_OF_PEOPLE)

mu = 200
sigma = 50

end = ','


file_person.write(INSERT_SCHEMA.format(PERSON_HEADER))
file_person.write(VALUES)

crypt_out = []

for i in range(0,NUMBER_OF_PEOPLE):
    
    #  generate person info
    # id, country, job, income, comfort_income, preferred_crypto
    id = i+1

    if id == NUMBER_OF_PEOPLE:
        end = ";"

    income = random.choices(income_ranges, weights=dict_jobs[job[i]])[0]
    comfort_income = random.choices(income_ranges, weights=income_wgts)[0]

    file_person.write(PERSON_FORMAT.format(id=id, country=country[i], job=job[i], income=income,
            comfort_income=comfort_income, preferred_crypto=prefer_crypto[i], end=end))

    # generate crypto owning
    num_own = random.choices([0,1,2,3], weights=crypto_number_own_wgts)[0]
    crypt_set = set()
    while len(crypt_set) < num_own:
        crypt_ran = random.choices(cryptocurrencies, weights=crypto_own_wgts)[0]
        crypt_set.add(crypt_ran)
        

    # person_id, name, amount
    for c in crypt_set:
        amount = random.gauss(mu, sigma)
        crypt_out.append(CRYPTO_OWN_FORMAT.format(person_id=id, crypto_name=c, amount=amount))
        

file_person.write('\n')  
file_person.write(INSERT_SCHEMA.format(CRYPTO_OWN_HEADER))
file_person.write(VALUES)
end = ",\n"

for i in range(len(crypt_out)):
    if i+1 == len(crypt_out):
        end = ";\n"
    line = crypt_out[i]+end
    file_person.write(line)


