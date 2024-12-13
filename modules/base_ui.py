from abc import ABC, abstractmethod

from kivy.app import App


class BaseUIModule(App, ABC):
    """
    Abstract base class for an arcade controller UI
    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def build(self):
        """
        Create and return the main layout of the app.
        """
        pass

    @abstractmethod
    def on_window_resize(self, window, width, height):
        """
        Handle window resize events.
        """
        pass

    @abstractmethod
    def update_button_positions(self, size):
        """
        Update the positions of buttons based on the window size.
        """
        pass

    @abstractmethod
    def on_button_press(self, instance):
        """
        Handle a button press event.
        """
        pass

    @abstractmethod
    def on_button_release(self, instance):
        """
        Handle a button release event
        """
        pass
