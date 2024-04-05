from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import openai

class ChatApp(App):
    count = 1
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Answer display box
        self.answer_label = Label(text='Answer will appear here', size_hint=(1, 0.8))
        layout.add_widget(self.answer_label)

        # Question input field
        self.question_input = TextInput(hint_text='Ask a question...', size_hint=(0.8, 0.1))
        layout.add_widget(self.question_input)

        # Send button
        send_button = Button(text='Send', size_hint=(0.2, 0.1), on_press=self.send_question)
        layout.add_widget(send_button)

        return layout

    def send_question(self, instance):
        user_question = self.question_input.text
        # Process the user's question and get the answer (you can replace this logic)
        answer = self.get_answer(user_question)
        self.answer_label.text = answer

    def get_answer(self, question):
        API = ""
        openai.api_key = API
        completion =openai.Completion()

        if len(question)>1:
            def Answer(question):
                prompt = f'You : {question}\nAssistant : '
                response = completion.create(
                    model = "gpt-3.5-turbo-instruct",
                    prompt=prompt,
                    temperature = 0.5,
                    max_tokens = 60,
                    top_p = 0.3,
                    frequency_penalty = 0.5,
                    presence_penalty = 0)
                ans = response.choices[0].text.strip()
                return ans
            answer = Answer(question)
        else:
            answer = "Invalid Question !"

        return f"You asked: {question} \n A.I.: {answer}"

if __name__ == '__main__':
    ChatApp().run()
