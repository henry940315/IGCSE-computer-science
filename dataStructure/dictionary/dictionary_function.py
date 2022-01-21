student_score = {"Amy":89,"Henry":99,"Mike":55,"Eric":60,"Charlie":88}

#get Amy's score
Amy_score = student_score.get("Amy")
print(Amy_score)


#delete the score of Amy
student_score.pop("Amy")
print(student_score)


#add a new key to the dictionary
student_score["Ivan"] = 68
print(student_score)


