from abc import ABC
from pynput.keyboard import Controller, Key
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle

from modules.base_ui import BaseUIModule

BUTTON_NAMES_TOP = ["2", "4", "6"]
BUTTON_NAMES_BOTTOM = ["1", "3", "5", "7"]
SCRATCH_BUTTONS = ["SCRATCH_UP", "SCRATCH_DOWN"]
KEY_MAPPINGS = {
    "1": "z",
    "2": "s",
    "3": "x",
    "4": "d",
    "5": "c",
    "6": "f",
    "7": "v",
    "SCRATCH_UP": "u",
    "SCRATCH_DOWN": "j",
}

BUTTON_COLORS_TOP = (0.5, 0.5, 0.5, 1)
BUTTON_COLORS_BOTTOM = (1, 1, 1, 1)
SCRATCH_WIDTH = 225


class IIDXController(BaseUIModule, ABC):
    def __init__(self):
        super().__init__()
        self._keyboard = Controller()
        self.layout = None
        self.buttons = []
        self.scratch_buttons = []
        self.button_graphics = {}

    def build(self):
        self.layout = FloatLayout()

        # Create top row buttons
        for name in BUTTON_NAMES_TOP:
            button = Button(
                text=name,
                size_hint=(None, None),
                background_color=(0, 0, 0, 0),
                font_size=0,
                background_normal=''
            )
            button.bind(on_press=self.on_button_press)
            button.bind(on_release=self.on_button_release)
            self.buttons.append(button)
            self.layout.add_widget(button)

        # Create bottom row buttons
        for name in BUTTON_NAMES_BOTTOM:
            button = Button(
                text=name,
                size_hint=(None, None),
                background_color=(0, 0, 0, 0),
                font_size=0,
                background_normal=''
            )
            button.bind(on_press=self.on_button_press)
            button.bind(on_release=self.on_button_release)
            self.buttons.append(button)
            self.layout.add_widget(button)

        for name in SCRATCH_BUTTONS:
            button = Button(
                text=name,
                size_hint=(None, None),
                background_color=(1, 1, 1, 1),
                font_size=0,
                background_normal=''
            )
            button.bind(on_press=self.on_button_press)
            button.bind(on_release=self.on_button_release)
            self.scratch_buttons.append(button)
            self.layout.add_widget(button)

        self.update_button_positions(Window.size)
        Window.bind(on_resize=self.on_window_resize)

        return self.layout

    def on_window_resize(self, window, width, height):
        self.update_button_positions((width, height))

    def update_button_positions(self, size):
        width, height = size

        button_height = height / 3.5
        button_width = button_height / 2
        spacing = button_width * 1.3

        # Position scratch buttons
        self.scratch_buttons[0].size = (SCRATCH_WIDTH, height / 2)  # Top half
        self.scratch_buttons[0].pos = (0, height / 2)

        self.scratch_buttons[1].size = (SCRATCH_WIDTH, height / 2)  # Bottom half
        self.scratch_buttons[1].pos = (0, 0)

        # Center buttons in window
        total_width_top = (len(BUTTON_NAMES_TOP) - 1) * spacing + button_width
        start_x_top = (width - total_width_top) / 2

        top_y = height / 1.5
        for i, button in enumerate(self.buttons[:3]):
            x = start_x_top + i * spacing
            button.size = (button_width, button_height)
            button.pos = (x, top_y - button_height / 2)
            with button.canvas.before:
                button.canvas.before.clear()
                color = Color(*BUTTON_COLORS_TOP)
                rect = Rectangle(pos=button.pos, size=button.size)
                self.button_graphics[button] = (color, rect)

        total_width_bottom = (len(BUTTON_NAMES_BOTTOM) - 1) * spacing + button_width
        start_x_bottom = (width - total_width_bottom) / 2
        bottom_y = height / 3.0
        for i, button in enumerate(self.buttons[3:]):
            x = start_x_bottom + i * spacing
            button.size = (button_width, button_height)
            button.pos = (x, bottom_y - button_height / 2)
            with button.canvas.before:
                button.canvas.before.clear()
                color = Color(*BUTTON_COLORS_BOTTOM)
                rect = Rectangle(pos=button.pos, size=button.size)
                self.button_graphics[button] = (color, rect)

    def on_button_press(self, instance):
        self._keyboard.press(KEY_MAPPINGS[instance.text])
        print(f"{instance.text} pressed")

    def on_button_release(self, instance):
        self._keyboard.release(KEY_MAPPINGS[instance.text])
        print(f"{instance.text} released")
