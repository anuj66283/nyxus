import json
import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
    
    def display_question(self):
        print(self.question)
        print(f'A) {self.options["A"]}\t\tB) {self.options["B"]}\
              \nC) {self.options["C"]}\t\tD) {self.options["D"]}')

    def check_answer(self, answer):
        if self.options[answer] == self.correct_answer:
            return True
        return False

class Game:
    def __init__(self, question_f):
        self.players = {}
        self.questions = self.read_json(question_f)[:10:]

    def read_json(self, question_f):
        with open(question_f, 'r') as f:
            jsn = json.load(f)

        random.shuffle(jsn)
        return jsn

    def add_players(self, name, score=0):
        self.players[name] = score
        print("Player added")
    
    def increase_score(self, name):
        self.players[name] += 5
    
    def declare_winner(self):
        print(f'Winner is {max(self.players)} with a score of {self.players[max(self.players)]}')
        
gm = Game('questions.json')

gm.add_players('anuj')
gm.add_players('test')

idx = 0

for x in gm.questions:
    options = {k: v for k, v in x.items() if k.isupper()}
    qn = Question(x['question'], options, x[x['answer']])
    qn.display_question()

    idx = idx%len(gm.players)

    for player in gm.players:
        ans = input(f"{player} turn: ")

        if qn.check_answer(ans):
            idx += 1
            gm.increase_score(player)
            break

        print("Wrong answer")

    print(f"Correct answer {qn.correct_answer}")

gm.declare_winner()





