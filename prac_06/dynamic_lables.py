"""
Practical 6 Kivy
"""


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_labels = Label(text=name)
            temp_labels.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_labels)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = "{}'s number is {}".format(name, self.names[name])

    def clear_all(self):
        self.root.ids.entriesBox.clear_labels()


DynamicWidgetsApp().run()
