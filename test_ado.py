from utils.adolite import AdoLite
from utils.vars import *
from faker import Faker
from random import randint

MAX_PERSONS = 10_000

fake = Faker()
ado = AdoLite("test.db")

def initdb():
  ado.createdb()
  ado.run_sql_script_file(name="sql/test.sql")
  ado.print_error()

def load_hobbies(name:str):
  with open(file=name, mode='r', encoding='utf-8') as f:
    hobbies = f.read().split('\n')
    for name in hobbies:
      ado.run_sql_param(SQL_INSERT_HOBBY, (name,))
    ado.commit()
    ado.print_error()
    return  hobbies

def load_trades(name:str):
  with open(file=name, mode='r', encoding='utf-8') as f:
    trades = f.read().split('\n')
    for name in trades:
      ado.run_sql_param(SQL_INSERT_TRADE, (name,))
    ado.commit()
    ado.print_error()
    return trades

def load_countries(name:str):
  with open(file=name, mode='r', encoding='utf-8') as f:
    countries = f.read().split('\n')
    for name in countries:
      ado.run_sql_param(SQL_INSERT_COUNTRY, (name,))
    ado.commit()
    ado.print_error()
    return countries

def load_fnames(name:str):
  with open(file=name, mode='r', encoding='utf-8') as f:
    fnames = f.read().split('\n')
    return fnames

def load_lnames(name:str):
  with open(file=name, mode='r', encoding='utf-8') as f:
    lnames = f.read().split('\n')
    return lnames

def main():
  initdb()
  hobbies = load_hobbies("files/hobbies.txt")
  trades = load_trades("files/trades.txt")
  countries = load_countries("files/countries.txt")
  fnames = load_fnames("files/fnames.txt")
  lnames = load_lnames("files/lnames.txt")


  conteo = 0
  while conteo < MAX_PERSONS:

    hobby_id = randint(0, len(hobbies))+1
    country_id = randint(0, len(countries))+1
    trade_id = randint(0, len(trades))+1
    fname_id  = randint(0, len(fnames)-1)
    lname_id  = randint(0, len(lnames)-1)
    salary = randint(10000, 90000)
    # Una fecha de nacimiento
    dob = fake.date_time_between(start_date='-60y', end_date='-18y')  

    print(conteo, fname_id, lname_id, dob)
    ado.run_sql_param(SQL_INSERT_PERSON, 
      (
        fnames[fname_id], 
        lnames[lname_id],
        dob.date(), 
        salary, 
        country_id, 
        hobby_id, 
        trade_id
      )
    )
    ado.print_error()

    conteo+=1

  ado.commit()
  ado.closedb()

if __name__ == '__main__':
  main()
