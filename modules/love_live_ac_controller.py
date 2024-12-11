from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from math import pi, cos, sin
from modules.base_ui import BaseUIModule
import keyboard

class LoveLiveController(BaseUIModule):
    def build(self):
        self.layout = FloatLayout()
        self.num_buttons = 9
        self.buttons = []

        for i in range(self.num_buttons):
            button = Button(
                text=f"Button {i + 1}",
                size_hint=(None, None),
                background_color=(0.5, 0.8, 1, 1),
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

    def on_button_press(self, instance):
        """Change button appearance when pressed."""
        instance.background_color = (1, 0.5, 0.5, 1)
        print(f"{instance.text} pressed")

    def on_button_release(self, instance):
        """Revert button appearance when released."""
        instance.background_color = (0.5, 0.8, 1, 1) 
        print(f"{instance.text} released")

if __name__ == "__main__":
    LoveLiveController().run()
