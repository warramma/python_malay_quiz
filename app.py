#6/30/24
#import Question class
from Question import Question

#list of questions

quiz_questions = [
    '\nWater in Malay is: \na) main \nb) maa \nc) pani \nd) air',
    '\nSelamat pagi means: \na) Good night! \nb) Good morning! \nc) Good evening! \nd) Good afternoon!',
    '\nWhich is the Malay adverb for \'sometimes\'? \na) kadang-kadang \nb) jarang \nc) sentiasa \nd) selalu',
    '\nHow would you say this time in Malay? 4:30pm \na) pukul tiga empat puluh petang \nb) pukul empat sepuluh petang \nc) pukul empat tiga puluh petang'
]

quiz = {
    '1' : Question('#1' + quiz_questions[0], 'd'),
    '2' : Question('#2' + quiz_questions[1], 'b'),
    '3' : Question('#3' + quiz_questions[2], 'a'),
    '4' : Question('#4' + quiz_questions[3], 'c')
}

for question in quiz:
    quiz[question].ask_question()

