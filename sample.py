
#Now how do you display the keys only...
#Now to allow the use to choose a topic to study
for k,v in enumerate (Questions,start=1):
    #print(f' {k}) {v}')
chosen_topic=input("\n>>>")
if chosen_topic=='1':
#Now, how to access the questions in the dict
    for question,answer in Questions['VARIABLES']:
       input_answer=input(f'\n{question}\n')    
       if input_answer==answer:
         print('THAT IS CORRECT!')
       else:
         print(f'Sorry, the correct answer is {answer} not, {input_answer}')

elif chosen_topic=='2':
    for question,answer in Questions['ITERATIONS']:
        input_answer=input(f'{question}\n')
        if input_answer==answer:
           print('THAT IS CORRECT!')
        else:
           print(f'Sorry, the correct answer is {answer} not, {input_answer}')
elif chosen_topic=='3':
    for question,answer in Questions['NETWORK PROGRAMMING']:
        input_answer=input(f'{question}\n')
        if input_answer==answer:
            print('THAT IS CORRECT!')
        else:
            print(f'Sorry, the correct answer is {answer} not, {input_answer}')

#Now, allowing the user to input their answer, even correct ones are 
#are marked as wrong, because they are not identical!Use mutiple choice