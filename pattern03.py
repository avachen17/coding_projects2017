import driver 

def letter (row, col): 
   if (row < 20 and col < 10): 
      return 'X'
   else: 
      return 'O'

if __name__ == '__main__':
   driver.comparePatterns(letter) 
