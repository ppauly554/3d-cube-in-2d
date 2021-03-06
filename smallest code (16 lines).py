import pygame;pygame.init();W, H = 900, 900;window = pygame.display.set_mode((W, H))
class Cube:
    def __init__(self, x, y):self.x = x;self.y = y;self.center = (x, y)
    def line(self, joint):pygame.draw.line(window, (255, 255, 255), (self.x, self.y), (joint.x, joint.y), 5)
points = [Cube(W * 2 / 18, H * 4 / 18),Cube(W * 11 / 18, H * 4 / 18),Cube(W * 2 / 18, H * 13 / 18),Cube(W * 11 / 18, H * 13 / 18),Cube(W * 7 / 18, H * 4 / 18),Cube(W * 16 / 18, H * 4 / 18),Cube(W * 7 / 18, H * 13 / 18),Cube(W * 16 / 18, H * 13 / 18)];links = [(points[0], points[1], points[2], points[4]),(points[1], points[0], points[3], points[5]),(points[2], points[0], points[3], points[6]),(points[3], points[1], points[2], points[7]),(points[4], points[0], points[5], points[6]),(points[5], points[1], points[4], points[7]),(points[6], points[2], points[4], points[7]),(points[7], points[3], points[5], points[6])];clock = pygame.time.Clock();run = True
while run:
    clock.tick(60);pygame.display.flip();window.fill((0, 0, 0));mpos = pygame.mouse.get_pos();for point in points:point.x, point.y = point.center
    for point in range(len(points)):
        if point % 2:points[point].x -= mpos[0] - W // 2;points[point].y -= mpos[1] - H // 2
        else:points[point].x += mpos[0] - W // 2;points[point].y += mpos[1] - H // 2
    for group in range(len(links)):
        for connection in range(3):links[group][0].line(links[group][connection + 1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:run = False; pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:run = False;pygame.quit()
