fresh=int(input('enter the number of fresh loves purchased'))
old=int(input('enter the number of day old loaves purchased'))
print('regular price : Rs.185')
fresh_amt=(185*float(fresh))
old_amt=(185*0.4)*float(old)
total=fresh_amt+old_amt
print('Amount of new loaves : Rs',fresh_amt)
print('Amount of old loaves : Rs',old_amt)
print('total amount: Rs',total)
