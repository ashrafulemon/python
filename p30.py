#3.6 calculate hours minutes seconds
ts=11725

h=ts//(3600)
ts=ts%3600
m=ts//60
s=ts%60
print("{} hours ,{} minutes ,{} seconds".format(h,m,s))