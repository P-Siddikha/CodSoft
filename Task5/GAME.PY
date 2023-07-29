import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                'question': 'What is the capital of Australia?',
                'choices': ['A. Paris', 'B. Canberra', 'C. London', 'D. Madrid'],
                'answer': 'B'
            },
            {
                'question': 'What is the average surface temperature on Venus?',
                'choices': ['A. 460°C (860°F)', 'B. 380°C (860°F)', 'C. 450°C (820°F)', 'D. 460°C (820°F)'],
                'answer': 'A'
            },
            {
                'question': 'Who painted the Mona Lisa?',
                'choices': ['A. Vincent van Gogh', 'B. Pablo Picasso', 'C. Leonardo da Vinci', 'D. Michelangelo'],
                'answer': 'C'
            },
            {
                'question': 'What is the largest ocean in the world?',
                'choices': ['A. Atlantic Ocean', 'B. Pacific Ocean', 'C. Indian Ocean', 'D. Arctic Ocean'],
                'answer': 'B'
            }
            # Add more questions here
        ]
        self.score = 0
        self.total_questions = 4
        self.current_question = 0
        self.incorrect_choices = []

    def welcome_message(self):
        instructions = 'Instructions:\n\n' \
                       '1. Read each question carefully.\n' \
                       '2. Select the correct answer by clicking on the respective button.\n' \
                       '3. Click the "Submit" button to proceed.\n' \
                       '4. At the end of the quiz, your score and any incorrect choices will be displayed.'

        messagebox.showinfo('Welcome', f'Welcome to the Quiz Game!\n\n{instructions}')

    def display_question(self):
        question = self.questions[self.current_question]['question']
        choices = self.questions[self.current_question]['choices']

        question_label.config(text=question)
        for i in range(4):
            choice_buttons[i].config(text=choices[i])

    def evaluate_answer(self):
        user_answer = answer_var.get()
        correct_answer = self.questions[self.current_question]['answer']

        if user_answer == correct_answer:
            self.score += 1
        else:
            self.incorrect_choices.append({
                'question': self.questions[self.current_question]['question'],
                'user_choice': user_answer,
                'correct_answer': correct_answer
            })

        self.current_question += 1
        answer_var.set('')

        if self.current_question == self.total_questions:
            self.display_final_results()
        else:
            self.display_question()

    def display_final_results(self):
        result_text = f'Quiz completed!\nYour final score is {self.score} out of {self.total_questions}.\n\n'
        if self.incorrect_choices:
            result_text += 'Incorrect Choices:\n'
            for choice in self.incorrect_choices:
                result_text += f'Question: {choice["question"]}\n'
                result_text += f'Your Choice: {choice["user_choice"]}\n'
                result_text += f'Correct Answer: {choice["correct_answer"]}\n\n'
        else:
            result_text += 'No incorrect choices.\n'
        result_label.config(text=result_text)
        result_label.pack(pady=10)
        play_again_button.pack(pady=10)
        submit_button.config(state=tk.DISABLED)

    def play_again(self):
        self.score = 0
        self.current_question = 0
        self.incorrect_choices.clear()
        result_label.pack_forget()
        play_again_button.pack_forget()
        submit_button.config(state=tk.NORMAL)
        self.display_question()

    def start(self):
        self.welcome_message()
        self.display_question()

# Create the GUI
window = tk.Tk()
window.title('Quiz Game')
window.geometry('500x400')
window.configure(bg='violet')

question_label = tk.Label(window, text='', font=('Arial', 14), wraplength=400, bg='violet')
question_label.pack(pady=10)

answer_var = tk.StringVar()
choice_buttons = []
for i in range(4):
    button = tk.Button(window, text='', font=('Arial', 12), width=30, bg='white',
                       activebackground='lightblue', command=lambda idx=i: answer_var.set(chr(ord('A')+idx)))
    button.pack(pady=5)
    choice_buttons.append(button)

submit_button = tk.Button(window, text='Submit', font=('Arial', 12), width=20, bg='lightgreen', activebackground='green')
submit_button.pack(pady=10)

result_label = tk.Label(window, text='', font=('Arial', 14), bg='lightgray')
play_again_button = tk.Button(window, text='Play Again', font=('Arial',12), width=20, bg='lightblue', activebackground='blue')

# Create a single instance of QuizGame
game = QuizGame()

def evaluate_answer():
    game.evaluate_answer()

def play_again():
    game.play_again()

# Set the command for submit_button and play_again_button
submit_button.config(command=evaluate_answer)
play_again_button.config(command=play_again)

# Start the quiz game
game.start()

window.mainloop()