import mysql.connector as mysql
import timeit
import argparse

db_config = {"host": "localhost",
             "user": "root",
             "password": "password",
             "port": 3306}

def cleanup():
  try:
    sql = "drop database IF EXISTS benchmarking"
    con = get_connection()
    cur = con.cursor()
    cur.execute(sql)
    cur.close()
  except Exception as e:
    print(e)
  

def create_db():
  try:
    sql = "CREATE DATABASE benchmarking"
    con = get_connection()
    cur = con.cursor()
    cur.execute(sql)
    cur.close()
  except Exception as e:
    print(e)

def column_threshold(n=1015, size=1):
  """
    Mariyadb support up to 1k columns and also total row size should not exceed 65535 bytes
  """
  try:
    columns = ', '.join(f"col_{str(x).zfill(4)} VARCHAR({size})" for x in range(1, n+1))
    sql = f"CREATE TABLE benchmarking.test1 ({columns})"
    con = get_connection()
    cur = con.cursor()
    cur.execute(sql)
  except Exception as e:
    print(e)

def get_connection():
  try:
    print("Connecting to database")
    con = mysql.connect(**db_config)
    print(f"Server info: {con.get_server_info()}")
    return con
  except Exception as e:
    print(e)

def argumentParser():
  parser = argparse.ArgumentParser(description='Mariyadb Benchmarking tool')


if __name__ == "__main__":
    cleanup()
    create_db()
    column_threshold()
