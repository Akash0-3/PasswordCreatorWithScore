import string

password = 'Akash@$2003$'

score = 0

upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
special = any([1 if i in string.punctuation else 0 for i in password])
digits = any([1 if i in string.digits else 0 for i in password])

char = [upper_case,lower_case,special,digits]

leng = len(password)

if leng >=8 :
    score+=1

if leng >=10:
    score+=1

if leng>=12:
    score+=1
if leng > 20:
    score+=1

print(f"password length {str(leng)}, adding score {str(score)}")

if sum(char)>1:
    score+=1
if sum(char)>2:
    score+=1
if sum(char)>3:
    score+=1

print(f"password has {str(sum(char))} different characters types, adding score {str(score)}")

if score < 4:
    print(f"the password is quite weak! Score: {str(score)}")
elif score == 4:
    print(f"the password is OK! ! Score: {str(score)}")
elif 4 < score < 6:
    print(f"the password is pretty good! Score: {str(score)}")
elif score >= 6:
    print(f"the password is strong! Score: {str(score)}")





