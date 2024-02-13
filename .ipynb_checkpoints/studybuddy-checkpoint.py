#Allow the learner to choose which topic they want to study

print('WELCOME TO STUDYBUDDY!\n')
print('------------')
print('Please choose a topic you would like to learn today')

Questions={
    'VARIABLES': [['How can you convert a variable from one data type to another in python?',
                  ['type(variable_name)','switch(variable_name)','change(variable_name)','convert(variable_name)']]
                  ,['What is a variable?',[ 'A constant value' , 'A reserved keyword in Python',
                    'A placeholder for storing data' ,' A mathematical operation']]]
,

    'ITERATIONS':[['What is the difference between for and while loop?',
                ['while loops are used for indefinite iteration and for loops for definite iteration',
                'for loops are used for indefinite iteration and while loops for definite iteration', 
                'There is no difference between them', 
                'while" loops can only iterate over numbers, for loops can iterate over any data type']],
                ['How do you exit a loop prematurely in python?',
                ['break statement', 'exit statement', 'stop statement','range statement']]]            
                                             
            
}
#print(Questions['ITERATIONS'][0])
#Now let us allow a student to choose the topic
for k,v in enumerate (Questions,start=1):
    print(f' {k}) {v}')
chosen_topic=input("\n>>>")
