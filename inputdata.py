import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class TestGrid(GridLayout):
    def __init__(self, **kwargs):
        super(TestGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Nama Depan: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Nama Belakang : "))
        self.last = TextInput(multiline=False)
        self.inside.add_widget(self.last)

        self.inside.add_widget(Label(text="No.Telepon : "))
        self.phone = TextInput(multiline=False)
        self.inside.add_widget(self.phone)

        self.inside.add_widget(Label(text="Email : "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text ="submit", font_size = 40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self,instance):
        name = self.name.text
        last = self.last.text
        phone = self.phone.text
        email = self.email.text

        print("Nama Depan:", name,"Nama Belakang:", last,"No.Handphone:", phone,"Email :", email)
        self.name.text = ""
        self.last.text = ""
        self.phone.text = ""
        self.email.text = ""


class TestApp(App):
    def build(self):
        return TestGrid()

if __name__ == "__main__":
    TestApp().run()

