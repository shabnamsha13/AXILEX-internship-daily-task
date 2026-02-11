#perform set operations
set1={10,20,30,40}
set2={30,40,50,60}

print("set 1:",set1)
print("set 2:",set2)

print("union:",set1.union(set2))
print("intersection:",set1.intersection(set2))
print("difference:",set1.difference(set2))
print("symmetric_dference:",set1.symmetric_difference(set2))