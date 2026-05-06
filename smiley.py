from vendor.sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    PINK = (255,0,255)
    BLUE = (0,0,255)
    BLANK = (0, 0, 0)

    def __init__(self):
        self.window_name = f"{self.__class__.__name__} Smiley"
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat(window_name=self.window_name)

        Y = self.YELLOW
        G = self.GREEN
        R = self.RED
        W = self.WHITE
        B = self.BLUE
        P = self.PINK
        O = self.BLANK
        self.pixels = [
            O, G, G, G, G, G, G, O,
            P, Y, B, Y, Y, B, Y, P,
            P, Y, B, Y, Y, B, Y, P,
            P, Y, Y, Y, Y, Y, Y, P,
            P, Y, Y, Y, Y, Y, Y, P,
            P, Y, Y, Y, Y, Y, Y, P,
            P, Y, Y, Y, Y, Y, Y, P,
            O, W, W, W, W, W, W, O,
        ]

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)

