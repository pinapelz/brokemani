from math import cos, pi, sin

from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Ellipse, Color
from pynput.keyboard import Controller

from modules.base_ui import BaseUIModule

KEY_MAPPINGS = {
    "RHYTHM_1": "q",
    "RHYTHM_2": "w",
    "RHYTHM_3": "e",
    "RHYTHM_4": "r",
    "RHYTHM_5": "t",
    "RHYTHM_6": "y",
    "RHYTHM_7": "u",
    "RHYTHM_8": "i",
    "RHYTHM_9": "o",
}

BUTTON_COLOR = (1, 1, 1, 1)  # White

class LoveLiveController(BaseUIModule):

    def __init__(self):
        super().__init__()
        self._keyboard = Controller()
        self.button_graphics = {}

    def build(self):
        self.layout = FloatLayout()
        self.num_buttons = 9
        self.buttons = []

        for i in range(self.num_buttons):
            button = Button(
                text=f"RHYTHM_{9 - i}",
                size_hint=(None, None),
                background_color=(0, 0, 0, 0),
                font_size=0,
                background_normal=''
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
        """Update button positions to span the top width of the window."""
        width, height = size
        button_size = width / 10
        y_offset = height - height / 8
        radius = width / 2.5

        for i, button in enumerate(self.buttons):
            angle = pi * i / (self.num_buttons - 1)
            x = width / 2 + radius * cos(angle)
            y = y_offset - radius * sin(angle)

            button.size = (button_size, button_size)
            button.pos = (x - button_size / 2, y - button_size / 2)
            with button.canvas.before:
                button.canvas.before.clear()
                color = Color(*BUTTON_COLOR)
                ellipse = Ellipse(pos=button.pos, size=button.size)
                self.button_graphics[button] = (color, ellipse)

    def on_button_press(self, instance):
        """Change button appearance when pressed."""
        color, _ = self.button_graphics[instance]
        color.rgba = (1, 0.5, 0.5, 1)
        self._keyboard.press(KEY_MAPPINGS[instance.text])
        print(f"{instance.text} pressed")

    def on_button_release(self, instance):
        """Revert button appearance when released."""
        color, _ = self.button_graphics[instance]
        color.rgba = BUTTON_COLOR
        self._keyboard.release(KEY_MAPPINGS[instance.text])
        print(f"{instance.text} released")

if __name__ == "__main__":
    LoveLiveController().run()