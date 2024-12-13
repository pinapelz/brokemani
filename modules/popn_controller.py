from pynput.keyboard import Controller
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

from modules.base_ui import BaseUIModule

BUTTON_NAMES_TOP = ["YELLOW_L", "BLUE_L", "BLUE_R", "YELLOW_R"]
BUTTON_NAMES_BOT = ["WHITE_L", "GREEN_L", "RED", "GREEN_R", "WHITE_R"]

KEY_MAPPINGS = {
    "WHITE_L": "x",
    "YELLOW_L": "d",
    "GREEN_L": "c",
    "BLUE_L": "f",
    "RED": "v",
    "BLUE_R": "g",
    "GREEN_R": "b",
    "YELLOW_R": "h",
    "WHITE_R": "n"
}

class PopnMusicController(BaseUIModule):
    """
    Builds the controller UI for Popn Music
    """

    def __init__(self):
        super().__init__()
        self._keyboard = Controller()

    def build(self):
        self.layout = FloatLayout()
        self.num_buttons_bottom = 5
        self.num_buttons_top = 4
        self.buttons = []

        for i in range(self.num_buttons_bottom):
            button = Button(
                text=f"{BUTTON_NAMES_BOT[i]}",
                size_hint=(None, None),
                background_color=(0.5, 0.8, 1, 1),
                font_size=20,
            )
            button.bind(on_press=self.on_button_press)
            button.bind(on_release=self.on_button_release)
            self.buttons.append(button)
            self.layout.add_widget(button)

        for i in range(self.num_buttons_top):
            button = Button(
                text=f"{BUTTON_NAMES_TOP[i]}",
                size_hint=(None, None),
                background_color=(0.8, 0.5, 1, 1),
                font_size=20,
            )
            button.bind(on_press=self.on_button_press)
            button.bind(on_release=self.on_button_release)
            self.buttons.append(button)
            self.layout.add_widget(button)

        self.update_button_positions(Window.size)
        Window.bind(on_resize=self.on_window_resize)
        return self.layout

    def on_window_resize(self, window, width, height):
        self.update_button_positions((width, height))

    def update_button_positions(self, size):
        width, height = size
        button_size = width / 8
        spacing = button_size * 1.4

        bottom_y = height / 4
        for i in range(self.num_buttons_bottom):
            x = width / 2 - ((self.num_buttons_bottom - 1) * spacing) / 2 + i * spacing
            button = self.buttons[i]
            button.size = (button_size, button_size)
            button.pos = (x - button_size / 2, bottom_y - button_size / 2)

        top_y = height / 1.7
        for i in range(self.num_buttons_top):
            x = width / 2 - ((self.num_buttons_top - 1) * spacing) / 2 + i * spacing
            button = self.buttons[self.num_buttons_bottom + i]
            button.size = (button_size, button_size)
            button.pos = (x - button_size / 2, top_y - button_size / 2)

    def on_button_press(self, instance):
        instance.background_color = (1, 0.5, 0.5, 1)
        self._keyboard.press(KEY_MAPPINGS[instance.text])
        print(f"{instance.text} pressed")

    def on_button_release(self, instance):
        instance.background_color = (0.5, 0.8, 1, 1)
        self._keyboard.release(KEY_MAPPINGS[instance.text])
        print(f"{instance.text} released")


if __name__ == "__main__":
    PopnMusicController().run()
