from pynput.keyboard import Controller
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Ellipse, Color

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

BUTTON_COLOR_TOP = [
    (1, 1, 0, 1), # Yellow
    (0, 0, 1, 1), # Blue
    (0, 0, 1, 1),
    (1, 1, 0, 1)
]

BUTTON_COLOR_BOT = [
    (1, 1, 1, 1), # White
    (0, 1, 0, 1), # Green
    (1, 0, 0, 1), # Red
    (0, 1, 0, 1),
    (1, 1, 1, 1)
]

class PopnMusicController(BaseUIModule):
    def __init__(self):
        super().__init__()
        self._keyboard = Controller()
        self.button_graphics = {}

    def build(self):
        self.layout = FloatLayout()
        self.num_buttons_bottom = 5
        self.num_buttons_top = 4
        self.buttons = []

        for i in range(self.num_buttons_bottom):
            button = Button(
                text=f"{BUTTON_NAMES_BOT[i]}",
                size_hint=(None, None),
                background_color=(0, 0, 0, 0),
                font_size=0,
                background_normal=''
            )
            button.bind(on_press=self.on_button_press)
            button.bind(on_release=self.on_button_release)
            self.buttons.append(button)
            self.layout.add_widget(button)

        for i in range(self.num_buttons_top):
            button = Button(
                text=f"{BUTTON_NAMES_TOP[i]}",
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
        width, height = size
        button_size = width / 7.5
        spacing = button_size * 1.4

        bottom_y = height / 4
        for i in range(self.num_buttons_bottom):
            x = width / 2 - ((self.num_buttons_bottom - 1) * spacing) / 2 + i * spacing
            button = self.buttons[i]
            button.size = (button_size, button_size)
            button.pos = (x - button_size / 2, bottom_y - button_size / 2)
            with button.canvas.before:
                button.canvas.before.clear()
                color = Color(*BUTTON_COLOR_BOT[i])
                ellipse = Ellipse(pos=button.pos, size=button.size)
                self.button_graphics[button] = (color, ellipse)

        top_y = height / 1.9
        for i in range(self.num_buttons_top):
            x = width / 2 - ((self.num_buttons_top - 1) * spacing) / 2 + i * spacing
            button = self.buttons[self.num_buttons_bottom + i]
            button.size = (button_size, button_size)
            button.pos = (x - button_size / 2, top_y - button_size / 2)
            with button.canvas.before:
                button.canvas.before.clear()
                color = Color(*BUTTON_COLOR_TOP[i])
                ellipse = Ellipse(pos=button.pos, size=button.size)
                self.button_graphics[button] = (color, ellipse)

    def on_button_press(self, instance):
        color, _ = self.button_graphics[instance]
        color.rgba = (1, 0.5, 0.5, 1)
        self._keyboard.press(KEY_MAPPINGS[instance.text])
        print(f"{instance.text} pressed")

    def on_button_release(self, instance):
        color, _ = self.button_graphics[instance]
        if instance.text in BUTTON_NAMES_BOT:
            index = BUTTON_NAMES_BOT.index(instance.text)
            color.rgba = BUTTON_COLOR_BOT[index]
        else:
            index = BUTTON_NAMES_TOP.index(instance.text)
            color.rgba = BUTTON_COLOR_TOP[index]
        self._keyboard.release(KEY_MAPPINGS[instance.text])
        print(f"{instance.text} released")
