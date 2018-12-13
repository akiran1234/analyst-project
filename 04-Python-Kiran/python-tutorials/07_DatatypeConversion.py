# Data type conversion.
# Implicit Data type Conversion and Explicit Data type Conversion.

a=10                             # int value
b=20.55                          # float value
c=a+b                            # This is implicit data type conversion result is float
print("C value is={0} and it's datatype={1}".format(c,type(c)))

print(float(a),type(a))          # This is explicit data type conversion using float method. int--> float
print(int(b),type(b))            # This is explicit, converting from float-->int
print(c,type(c),type(str(c)))    # This is explicit, converting from float-->str


l=[10,20.34,40,'Linux']
s=str(l)                         # Converting list to string data type.
print("This is String:",s,type(s),s[:3])

s1="Hello String"
l1=list(s1)                      # Every character will become each list item.
print("This is List:",l1,type(l1))

t1=(10,20,30,40.50,'String')
l2=list(t1)                      # Converting to list from tuple.
print("This is list from tuple:",l2,type(l2))

t2=tuple(l)                      # Converting to tuple from list.
print("This is tuple from list l",t2,type(t2))

set1=set(t2)
print("This is set from tuple t2",set1,type(set1))