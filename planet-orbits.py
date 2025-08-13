import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
clock = pygame.time.Clock()

G = 6.67430e-11  # Gravitational constant
SCALE = 6e-11  # Scale for outer solar system view (meters to pixels)
ZOOM_SCALE = 1e-9  # Scale for inner solar system view
DT = 86400  # Time step (delta time): 1 day in seconds

zoomed = False  # Toggles between SCALE and ZOOM_SCALE


class Body:
    def __init__(self, x, y, vx, vy, mass, radius, color):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.mass = mass
        self.radius = radius
        self.color = color
        self.trail = []

    def update_position(self, bodies):
        # Calculates gravitational force from all other bodies and updates position.
        fx = fy = 0
        for other in bodies:
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                r = math.sqrt(dx * dx + dy * dy)
                if r > 0:
                    # Formula: F = G * (m1 * m2) / r^2
                    f = G * self.mass * other.mass / (r * r)
                    fx += f * dx / r
                    fy += f * dy / r

        # Formula: a = F / m  (based on F = ma)
        ax = fx / self.mass
        ay = fy / self.mass
        # Update velocity based on acceleration over the time step
        self.vx += ax * DT
        self.vy += ay * DT
        # Update position based on new velocity over the time step
        self.x += self.vx * DT
        self.y += self.vy * DT

        # Determine the current scale for drawing
        current_scale = ZOOM_SCALE if zoomed else SCALE

        self.trail.append(
            (
                int(self.x * current_scale + WIDTH // 2),
                int(self.y * current_scale + HEIGHT // 2),
            )
        )

        # Keep the trail from getting too long
        if len(self.trail) > 200:
            self.trail.pop(0)

    def draw(self, screen):
        # Draws the body and its trail onto the screen.
        if len(self.trail) > 1:
            pygame.draw.lines(screen, (50, 50, 50), False, self.trail, 1)

            current_scale = ZOOM_SCALE if zoomed else SCALE

            screen_x = int(self.x * current_scale + WIDTH // 2)
            screen_y = int(self.y * current_scale + HEIGHT // 2)

            # Draw the body itself as a circle
            pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.radius)


bodies = [
    Body(0, 0, 0, 0, 1.989e30, 16, (255, 255, 0)),  # Sun
    Body(5.79e10, 0, 0, 47360, 3.301e23, 4, (169, 169, 169)),  # Mercury
    Body(1.082e11, 0, 0, 35020, 4.867e24, 6, (255, 165, 0)),  # Venus
    Body(1.496e11, 0, 0, 29780, 5.972e24, 8, (0, 100, 255)),  # Earth
    Body(279e11, 0, 0, 24077, 6.39e23, 5, (255, 100, 0)),  # Mars
    Body(7.786e11, 0, 0, 13070, 1.898e27, 12, (200, 150, 100)),  # Jupiter
    Body(1.432e12, 0, 0, 9680, 5.683e26, 11, (250, 200, 100)),  # Saturn
    Body(2.867e12, 0, 0, 6810, 8.681e25, 6, (100, 200, 255)),  # Uranus
    Body(4.515e12, 0, 0, 5430, 1.024e26, 6, (0, 0, 255)),  # Neptune
    Body(5.906e12, 0, 0, 4670, 1.309e22, 3, (150, 100, 50)),  # Pluto
]


running = True
while running:
    # Event handling (e.g., closing window, key presses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                zoomed = not zoomed
            for body in bodies:
                body.trail = []

    screen.fill((0, 0, 0))

    # Update and draw each body for the current frame
    for body in bodies:
        body.update_position(bodies)
        body.draw(screen)

    # Refresh the entire display
    pygame.display.flip()
    # Limit the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
