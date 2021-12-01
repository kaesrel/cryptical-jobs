import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from autogen.openapi_server import models


def db_cursor():
    return mysql.connect(host=DB_HOST,
                         user=DB_USER,
                         passwd=DB_PASSWD,
                         db=DB_NAME).cursor()

def get_income():
    with db_cursor() as cs:
        cs.execute("""
                SELECT job, AVG(income_value) as avg_income, country
                FROM Person_mapped
                GROUP BY job, country
            """)
        result = cs.fetchall()
        list_income = []
        for row in result:
            job, income, country = row
            data = {"job": job, "income": income, "country": country}
            list_income.append(data)
        return list_income


def get_income_job(job):
    with db_cursor() as cs:
        cs.execute("""
                    SELECT job, AVG(income_value) AS avg_income
                    FROM Person_mapped as P
                    WHERE P.job = %s
                    GROUP BY job
            """, [job])
        result = cs.fetchone()
        job, income = result
        data = {"job": job, "income": income}
        return data


def get_income_country(country):
    with db_cursor() as cs:
        cs.execute("""
                SELECT country, AVG(income_value) AS avg_income
                FROM Person_mapped as P
                WHERE P.country = %s
                GROUP BY country
            """, [country])
        result = cs.fetchone()
        country, income = result
        data = {"country": country, "income": income}
        return data


def get_income_country_job(country, job):
    with db_cursor() as cs:
        cs.execute("""
                SELECT AVG(income_value) as avg_income
                FROM Person_mapped as P
                WHERE P.job = %s and P.country = %s
            """, [job, country])
        result = cs.fetchone()
        income = result
        data = {"income": income[0]}
        return data


def get_income_world():
    with db_cursor() as cs:
        cs.execute("""
                SELECT job, country, income 
                FROM AverageIncome
            """)
        result = cs.fetchall()
        list_income = []
        for row in result:
            job, country, income = row
            data = {"job": job, "income": income, "country": country}
            list_income.append(data)
        return list_income


def get_prefer_crypto():
    with db_cursor() as cs:
        cs.execute("""
                SELECT P.preferred_crypto as crypto_name, COUNT(P.preferred_crypto) AS crypto_count 
                FROM Person_mapped as P
                GROUP BY P.preferred_crypto
            """)
        result = cs.fetchall()
        list_income = []
        for row in result:
            name, count = row
            data = {"name": name, "count": count}
            list_income.append(data)
        return list_income


def get_crypto():
    with db_cursor() as cs:
        cs.execute("""
                SELECT CO.name, AVG(CO.amount) as avg_amount 
                FROM Person_mapped as P, CryptoOwn as CO 
                WHERE P.id = CO.person_id 
                GROUP BY CO.name
            """)
        result = cs.fetchall()
        list_income = []
        for row in result:
            name, count = row
            data = {"name": name, "amount": count}
            list_income.append(data)
        return list_income


def get_crypto_country():
    with db_cursor() as cs:
        cs.execute("""
                SELECT P.country, CO.name, AVG(CO.amount) as avg_amount
                FROM Person_mapped as P, CryptoOwn as CO
                WHERE P.id = CO.person_id
                GROUP BY P.country, CO.name
            """)
        result = cs.fetchall()
        list_income = []
        for row in result:
            country, name, amount = row
            data = {"country": country, "name": name, "amount": amount}
            list_income.append(data)
        return list_income


def get_crypto_income():
    with db_cursor() as cs:
        cs.execute("""
                SELECT P.income_value, CO.name, AVG(CO.amount) as avg_amount
                FROM Person_mapped as P, CryptoOwn as CO
                WHERE P.id = CO.person_id
                GROUP BY P.income_value, CO.name
            """)
        result = cs.fetchall()
        list_income = []
        for row in result:
            income, name, amount = row
            data = {"income": income, "name": name, "amount": amount}
            list_income.append(data)
        return list_income
