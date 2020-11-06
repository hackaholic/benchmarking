import memcache
import timeit
import sys
import argparse

server = "localhost:11211"
size, n, t = 2, 100, ""
payload = "\0"

  
def mem_con():
  return memcache.Client([server])

def flush(mc):
  mc.flush_all()

def set_val(mc, key, size):
  mc.set(key, payload)
  
def get_val(mc, key):
  return mc.get(key)

def basic_test():
  mc = mem_con()

def argumentParser():
  parser = argparse.ArgumentParser(description='Memcached Benchmarking tool')
  parser.add_argument("-n", action="store", type=int, help="Number of requests to perform, default 100")
  parser.add_argument("-t", action="store", type=str, help="Multiple operation seperated by comma")
  parser.add_argument("-s", action="store", type=int, help="value size in bytes, by default its 2 bytes")
  return parser

def main():
  global size, n, t, payload
  argparser = argumentParser()
  args = argparser.parse_args()
  size = args.s if args.s else size
  n = args.n if args.n else n
  t = args.t if args.t else t
  payload = payload*size
  print("Performing Memcached benchmarking....")
  t = timeit.timeit(f"set_val(mc,'hello', payload)", setup="from __main__ import set_val,payload,mem_con,size; mc = mem_con()", number=n)
  print(f"time taken to set value of key of size:{size}, for {n} times, {t} secs")
  t = timeit.timeit(f"get_val(mc,'hello')", setup="from __main__ import set_val,get_val,mem_con; mc = mem_con()", number=n)
  print(f"time taken to get value of key for {n} times, {t} secs")
  
  
if __name__ == '__main__':
  main()
