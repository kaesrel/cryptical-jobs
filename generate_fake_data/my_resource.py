countries = [ "US", "UK", "China", "Thailand", "Japan" ]

income_ranges = ['5k_or_less', '10k', '25k', '50k',
        '100k', '200k', '500k', '1000k_or_more']

cryptocurrencies = [
    "Bitcoins (BTC)",
    "Ethereum (ETH)",
    "Binance Coin (BNB)",
    "Tether (USDT)",
    "Dogecoin (DOGE)",
    "None"
]

dict_jobs = {
    'Office Worker': (1,3,5,4,1,0,0,0),
    'Engineer':     (0,1,3,7,5,2,0,0),
    'Janitor':      (3,2,1,1,0,0,0,0),
    'Receptionist': (1,2,3,2,1,0,0,0),
    'Sales Clerk': (1,2,3,2,1,0,0,0),
    'Mechanic': (1,4,3,2,1,0,0,0),
    'Teacher': (1,3,9,21,12,4,0,0),
    'Manager': (0,0,3,10,8,3,1,0),
    'Musician': (1,3,4,3,2,1,1,1),
    'Political Staff': (0,0,1,2,5,4,2,1),
    'Media Staff (eg. news reporter)': (0,1,2,4,2,1,0,0),
    'Artist': (1,3,2,2,2,1,2,3),
}


job_wgts = (20,5,8,10,10,8,10,4,5,2,5,4)
country_wgts = (4, 3, 2, 10, 3)
income_wgts = (1,3,5,4,3,2,1,1)
crypto_own_wgts = (5,2,1,2,3,0)
crypto_prefer_wgts = (5,2,1,2,3,5)

crypto_number_own_wgts = (8, 4, 3, 1)


INSERT_SCHEMA = "INSERT INTO {}\n"
VALUES = "VALUES\n"

PERSON_HEADER = "Person(id, country, job, income, comfort_income, preferred_crypto)"
CRYPTO_OWN_HEADER = "CryptoOwn(person_id, name, amount)"

PERSON_FORMAT = "({id}, '{country}', '{job}', '{income}'," \
        " '{comfort_income}', '{preferred_crypto}'){end}\n"

CRYPTO_OWN_FORMAT = "('{person_id}', '{crypto_name}', '{amount}')"



















