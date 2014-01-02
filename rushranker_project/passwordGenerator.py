import random

def passwords():
   letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
   for n in range(1,150):
      p=""
      for i in range(1,8):
         p+=(random.choice(letters))
      print p


if __name__ == '__main__':
   passwords()