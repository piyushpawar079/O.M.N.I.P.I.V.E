import pygame


class Pong:
    def main(self):
        pygame.init()

        # Colors
        white = (255, 255, 255)
        screen_weight = 800
        screen_height = 600
        bg = (0, 0, 0)

        # Define Game Variable
        margin = 50
        cpu_win = 0
        live_ball = False
        winner = 0
        player_win = 0
        speed_increase = 0

        def draw_board(screen):
            screen.fill(bg)
            pygame.draw.line(screen, white, (0, margin), (screen_weight, margin))

        def draw_text(text,font, text_col, x, y, screen):
            img = font.render(text, True, text_col)
            screen.blit(img, (x, y))

        class Paddle:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.rect = pygame.Rect(x, y, 20, 100)
                self.speed = 5

            def move(self):
                key = pygame.key.get_pressed()

                if key[pygame.K_UP] and self.rect.top > margin:
                    self.rect.move_ip(0, -1 * self.speed)
                if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
                    self.rect.move_ip(0, self.speed)

            def draw(self, screen):
                pygame.draw.rect(screen, white, self.rect)

            def ai(self, game_ball):

                if self.rect.centery < game_ball.rect.top and self.rect.bottom < screen_height:
                    self.rect.move_ip(0, self.speed)
                if self.rect.centery > game_ball.rect.bottom and self.rect.top > margin:
                    self.rect.move_ip(0, -1 * self.speed)

        class Ball:
            def __init__(self, x, y):
                self.reset(x, y)

            def draw(self, screen):
                pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)

            def move(self, player_paddle, cpu_paddle):

                if self.rect.bottom > screen_height or self.rect.top < margin + 10:
                    self.speed_y *= -1

                if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
                    self.speed_x *= -1

                if self.rect.left < 0:
                    self.winner = 1
                elif self.rect.right > screen_weight:
                    self.winner = -1

                self.rect.x += self.speed_x
                self.rect.y += self.speed_y

                return self.winner

            def reset(self, x, y):
                self.x = x
                self.y = y
                self.ball_rad = 8
                self.rect = pygame.Rect(x, y, 16, 16)
                self.speed_x = -4
                self.speed_y = 4
                self.winner = 0


        font = pygame.font.SysFont('Constantia', 30)

        pygame.display.set_caption('Ping Pong')

        screen = pygame.display.set_mode((screen_weight, screen_height))

        clock = pygame.time.Clock()

        game_ball = Ball(screen_weight - 25, margin + 20)

        player_paddle = Paddle(screen_weight - 15, margin)
        cpu_paddle = Paddle(-5, margin)

        while True:

            draw_board(screen)
            draw_text('CPU: '+str(cpu_win), font, white, 10, 10, screen)
            draw_text('Player: '+str(player_win), font,  white, screen_weight - 130, 10, screen)
            draw_text('Speed: '+str(abs(game_ball.speed_x)), font, white, screen_weight // 2 - 10, 10, screen)

            player_paddle.draw(screen)
            cpu_paddle.draw(screen)

            if live_ball:
                speed_increase += 1
                winner = game_ball.move(player_paddle, cpu_paddle)
                if not winner:
                    game_ball.draw(screen)
                    player_paddle.move()
                    cpu_paddle.ai(game_ball)
                else:
                    live_ball = False
                    if winner == 1:
                        player_win += 1
                    else:
                        cpu_win += 1

            if not live_ball:
                if not winner:
                    draw_text('Click to start the game', font, white, screen_weight // 2 - 100, screen_height // 2 - 100, screen)
                if winner == 1:
                    draw_text('You scored point', font, white, screen_weight // 2 - 100, screen_height // 2 - 200, screen)
                    draw_text('Click to start the game', font, white, screen_weight // 2 - 100, screen_height // 2 -100, screen)
                if winner == -1:
                    draw_text('CPU scored point', font, white, screen_weight // 2 - 100, screen_height // 2 - 200, screen)
                    draw_text('Click to start the game', font, white, screen_weight // 2 - 100, screen_height // 2 - 100, screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and not live_ball:
                    live_ball = True
                    game_ball.reset(screen_weight - 25, margin + 20)

            if speed_increase > 300:
                speed_increase = 0
                cpu_paddle.speed += 2
                if game_ball.speed_x < 0:
                    game_ball.speed_x -= 1
                if game_ball.speed_x > 0:
                    game_ball.speed_x += 1
                if game_ball.speed_y < 0:
                    game_ball.speed_y -= 1
                if game_ball.speed_y > 0:
                    game_ball.speed_y += 1

            try:
                pygame.display.update()
            except pygame.error:
                break
            clock.tick(60)


if __name__ == '__main__':
    pong = Pong()
    pong.main()
