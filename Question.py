class Question:
    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        #self.score = 0
    
    def ask_question(self):
        answer = input(self.prompt + '\n')
        return answer
        #answer = 
        #if (answer == self.answer.lower() or answer == self.answer.upper()):
           # score += 1
    #def display_score():
        #print(self.score)

