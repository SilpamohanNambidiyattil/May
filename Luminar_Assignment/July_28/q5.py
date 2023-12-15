""" 5.Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they ty
pe it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the ans
wer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not an
swer yes to the first question, display the answer “Enjoy your day”."""

user_input1=input('if it is raining:')
user_ans_lower1=user_input1.lower()
if user_ans_lower1=='yes':
    user_input2=input('if it is windy :')
    user_ans_lower2=user_input2.lower()
    if user_ans_lower2=='yes':
        print('It is too windy for an umberlla')
    else:
        print('Take an umberlla')
else:
    print('Enjoy your day')


""" 
OUTPUT1
if it is raining:yes
if it is windy :yes
It is too windy for an umberlla

OUTPUT2
if it is raining:YES
if it is windy :no
Take an umberlla

OUTPUT3
if it is raining:no
Enjoy your day
"""