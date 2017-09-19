from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('m_to_km.kv')
        return self.root

    def handle_increment(self, miles, increment):
        miles = miles_to_int(miles)
        miles += increment
        self.root.ids.input_number.text = str(miles)

    def m_to_km(self, miles):
        miles = miles_to_int(miles)
        result = 1.6 * miles
        self.root.ids.converted_value.text = "{:.2f}".format(result)


def miles_to_int(number):
    try:
        return int(number)
    except ValueError:
        return 0

SquareNumberApp().run()