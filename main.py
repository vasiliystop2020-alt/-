
from kiwi.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from deep_translator import GoogleTranslator

class NexusTranslatorApp(App):
    def build(self):
        self.title = "NEXUS Translator v1.0"
        
        # Главный контейнер (элементы идут сверху вниз)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Название приложения на экране
        layout.add_widget(Label(text="NEXUS TRANSLATOR", font_size=24, size_hint_y=None, height=40))
        
        # Поле для ввода текста
        self.input_text = TextInput(hint_text="Введите текст для перевода...", multiline=True)
        layout.add_widget(self.input_text)
        
        # Поле для ввода языка (например, en, ru)
        self.lang_text = TextInput(hint_text="Код языка (en, ru, es, de)...", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.lang_text)
        
        # Кнопка "Перевести"
        btn = Button(text="ПЕРЕВЕСТИ", background_color=[0, 0.7, 1, 1], size_hint_y=None, height=60)
        btn.bind(on_press=self.translate_text) # Привязываем функцию перевода к кнопке
        layout.add_widget(btn)
        
        # Поле вывода результата
        self.result_label = Label(text="Здесь появится перевод", font_size=18, halign="center")
        layout.add_widget(self.result_label)
        
        return layout

    def translate_text(self, instance):
        text = self.input_text.text
        lang = self.lang_text.text.strip().lower()
        
        if not text or not lang:
            self.result_label.text = "Заполните все поля!"
            return
            
        try:
            # Выполняем перевод через интернет
            translated = GoogleTranslator(source='auto', target=lang).translate(text)
            self.result_label.text = translated
        except Exception:
            self.result_label.text = "Ошибка! Проверьте интернет или код языка."

if __name__ == "__main__":
    NexusTranslatorApp().run()
