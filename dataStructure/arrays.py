from array import array 


#create a new array using built in array mwthod
test_score = array("i",[98,78,48,55,66,77])
#add another test score to our array
test_score.append(100)

#add another test score to start of the array (position 0)
test_score.insert(98)

#delete a number from our array
test_score.remove(55)

for score in test_score:
    print(score)

#get length of the array
length = len(test_score)
print("length of the array", length)

#other array method
first_value = test_score.remove[98]


