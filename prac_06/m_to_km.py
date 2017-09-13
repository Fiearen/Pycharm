from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('m_to_km.kv')
        return self.root

    def handle_increment(self, value):
        self.root.ids.input_number.text += value

    def handle_calculate(self, value):
        result = value/1000
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()