#Unpacking a Sequence into Separate Variables
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name,shares,price,date=data
print(name)
print(shares)
print(price)
print(date)
#Unpacking actually works with any object that happens to be iterable, not just tuples or lists. This includes strings, files, iterators, and generators. 
# For example:
s='hello'
a,b,c,d,e=s
print(a)
print(b)
print(c)
print(d)
print(e)


#Unpacking Elements from Iterables of Arbitrary Length

#Python “star expressions” 

data2 =('payal','abc@email.com','dungeon ally',[790111 , 345678])
name,email,address,*phone_num=data2
print(name)
print(email)
print(address)
print(phone_num)







