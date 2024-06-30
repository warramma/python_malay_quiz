class Question:

    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    
    def display_question(self):
        print(self.prompt)