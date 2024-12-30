import pygame
import typing


class GameElement:
    """
    A GameElement is an updatable and drawable entity. It has a pygame.Rect
    attribute called rect that  has x and y positions (as well as the topleft,
    bottom, etc. variables that Rect objects have). It also has an image
    (instantiated with a filename), and a velocity in 2D space.

    Public Methods
    --------------
    update(dt, events, screen)
        Update the position of the GameElement based on its velocity and the
        time delta.

    collided_with(other_element)
        Handle behavior when this element collides with another.

    draw(screen)
        Draw this object's image on the given screen surface at its current
        position.

    Public Instance Variables
    -------------------------
    collidable : bool
        True if this element can be collided with and should participate in
        collision detection calculations.

    rect : pygame.Rect
        The rectangular area that defines the position and size of the
        GameElement. This can be used to query and set attributes like
        rect.center.

    velocity : pygame.math.Vector2
        The current velocity of this element on the screen in pixels per
        millisecond. The positive direction of a velocity vector is to the
        right and down (↘).

    Notes
    -----
    The x and y positions are always defined in pixels and refer to the top left
    corner of the image. The x and y values are always relative to the top left
    corner of the game screen itself, which is defined to be at x=0, y=0.

    The velocity is a pygame.math.Vector2 value in pixels per millisecond (ppm),
    with a unit vector pointing 1 ppm to the right and 1 ppm down (↘).

    The image file is expected to contain a single loadable image that can be
    drawn on the pygame screen. A single image can be selected from a sprite sheet
    of multiple images by using optional cropping parameters when instantiating
    the object

    While not required, it is expected that the update, collided_with, and draw
    methods are called once per frame, in the following order:

      1. update
      2. collided_with
      3. draw

    All of these methods are normally overridden in subclasses of this class,
    but this class' version can be used for simple elements.
    """
    def __init__(self,
                 image: typing.Union[str, pygame.Surface],
                 x: int = 0,
                 y: int = 0,
                 velocity: pygame.math.Vector2 = pygame.math.Vector2(0, 0),
                 collidable: bool = True):
        """
        :param image: The name of the file, including the relative path
                        to the file that contains the image to be displayed
                        for the element, or a pygame.Surface object. If the
                        name of a file is given, it is assumed to contain
                        alpha information for transparency. The surface
                        created from this image file will have the
                        convert_alpha method called on it to improve blit
                        performance.
        :param x: The initial horizontal position, in pixels, relative to the
                    top left of the screen, of the element.
        :param y: The initial vertical position, in pixels, relative to the
                    top left of the screen, of the element.
        :param velocity: The initial velocity, in pixels per millisecond,
                    of the element. The unit vector points to the right and
                    down.
        :param collidable: If True (the default) the element can be collided
                            with and should participate in collision detection
                            calculations. Set this to False for background
                            elements or anything that other elements can
                            pass through without hitting anything.

        TODO: Add support for cropping a single image out of a sprite sheet.
        """
        # Make sure pygame is initialized.
        if not pygame.get_init():
            raise RuntimeError(
                f"Pygame must be initialized before creating a {self.__class__.__name__} object. "
                f"Please call pygame.init() before using this class."
            )

        # Load the image if a file path is provided, otherwise use the provided surface
        if isinstance(image, str):
            self.image = pygame.image.load(image).convert_alpha()
        elif isinstance(image, pygame.Surface):
            self.image = image
        else:
            raise ValueError("The image parameter must be either a file path or a pygame.Surface object.")

        # Create the rect attribute
        self.rect = self.image.get_rect(topleft=(x, y))

        # Initialize other passed in settings
        self.velocity = velocity
        self.collidable = collidable

    def update(self, dt: int, events: typing.Optional[list[pygame.event.Event]] = None, screen: typing.Optional[pygame.Surface] = None, **kwargs):
        """
        Update the position of the GameElement based on its velocity and the time delta.

        Warning: If overridden, this method should be overridden completely.
                    (i.e. do NOT use super().update())

        :param dt: The number of milliseconds since the last call to update.
                    This is used with any movement calculations to help
                    smooth and jitter in the frame rate.
        :param events: A list of the pygame events detected since the last
                        frame. Not all elements care about events, so this
                        is optional and defaults None if omitted. When
                        overriding this method, the fact that the events can
                        be None MUST be taken into account if it is used.
        :param screen: The surface on which this GameElement will ultimately be
                        drawn. This can be used to determine if this element
                        will still be on the screen when drawn. Not all
                        elements care about the surface, so it is optional
                        and defaults to None if omitted. When overriding
                        this method, the fact that the screen can be None
                        MUST be taken into account if it is used.

        """
        self.rect.move_ip(self.velocity.x * dt, self.velocity.y * dt)

    def collided_with(self, other_element: 'GameElement'):
        """
        React to a collision with the specified "other_element".

        Override this method if the self object should be affected by
        collisions and use it to update the self instance only. Do not update
        the "other_instance". If the "other_instance" is also affected by the
        collision, its collided_with() method is the one that is responsible
        for updating that object.

        This method should be called whenever collisions occur.

        :param other_element: The GameElement object that collided with this
                                GameElement.
        """
        # TODO: Provide some generic reaction to collisions
        pass

    def draw(self, screen: pygame.Surface):
        """
        Draw this object's image on the given screen surface at its current position.

        Warning: If overridden, this method should be overridden completely.
                    (i.e. do NOT use super().update())

        :param screen: The display surface this GameElement is to be drawn in.
            The element's position is always relative to the top-left corner
            of the screen.
        """
        screen.blit(self.image, self.rect.topleft)
