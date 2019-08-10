from question import Question
class QuestionService:
    questions = []

    @classmethod
    def loadQuestions(cls):
        with open('questions.txt') as file:
            data = file.readlines()
            for line in data:
                q = line.split(',')
                cls.questions.append(Question(*q))

    @classmethod
    def beginQuiz(cls):
        cls.loadQuestions()
        n_correct = 0
        n_wrong = 0
        for i,quest in enumerate(cls.questions):
            print(f'{i+1} : {quest}')
            c = input('Enter your choice: ')
            if c == quest.ans.strip():
                n_correct += 1
            else:
                n_wrong += 1

        cls.show_result(n_correct,n_wrong)

    @classmethod
    def show_result(cls,correct,wrong):
        total_quest = len(cls.questions)
        print(f'Total questions: {total_quest}')
        print(f'Number of correct answers: {correct}')
        print(f'Number of wrong answers : {wrong}')

        perc = (correct/total_quest)*100
        if perc > 65:
            print('Party!!')
        else:
            print('Don\'t try again')
