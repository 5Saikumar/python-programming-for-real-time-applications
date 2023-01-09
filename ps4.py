def onedigit(num):
      return((num>=0) and (num<10))
def saikumar(num,dupnum):
      if onedigit(num):
            return(num==(dupnum[0])%10)
      if not saikumar(num//10,dupnum):
            return False
      dupnum[0]=dupnum[0]//10
      return (num%10==(dupnum[0])%10)
def sai(num):
      if (num<0):
            num=-num
      dupnum=[num]
      return saikumar(num,dupnum)
n=1234321
if  sai(n):
      print('yes')
else:
      print('no')

      
