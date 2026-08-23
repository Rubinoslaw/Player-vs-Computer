import pygame, random, asyncio, webbrowser



# Game loop
async def main():
    FPS = 40
    bg_color = [24, 25, 25]
    SCREEN_HEIGHT = 930
    SCREEN_WIDTH = 1070

    pygame.mixer.pre_init(frequency=43200, size=-16, channels=16, buffer=2048)
    pygame.init()

    pygame.display.set_caption("Player vs Computer")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Images
    paper_img = pygame.image.load("images/paper.png").convert_alpha()
    paper_img = pygame.transform.scale(paper_img, (130, 130))
    rock_img = pygame.image.load("images/rock.png").convert_alpha()
    rock_img = pygame.transform.scale(rock_img, (130, 130))
    scissors_img = pygame.image.load("images/scissors.png").convert_alpha()
    scissors_img = pygame.transform.scale(scissors_img, (130, 130))
    water_img = pygame.image.load("images/water.png").convert_alpha()
    water_img = pygame.transform.scale(water_img, (130, 130))
    gigachad_img = pygame.image.load("images/gigachad.png").convert_alpha()
    gigachad_img = pygame.transform.scale(gigachad_img, (185, 252))
    replay_img = pygame.image.load("images/replay.png").convert_alpha()
    replay_img = pygame.transform.scale(replay_img, (77, 77))
    github_logo = pygame.image.load("images/github.png").convert_alpha()
    github_logo = pygame.transform.scale(github_logo, (59, 59))
    website_img = pygame.image.load("images/website.png").convert_alpha()
    website_img = pygame.transform.scale(website_img, (75, 75))
    feedback_img = pygame.image.load("images/send_feedback.png").convert_alpha()
    feedback_img = pygame.transform.scale(feedback_img, (87, 87))
    youtube_logo = pygame.image.load("images/youtube.png").convert_alpha()
    youtube_logo = pygame.transform.scale(youtube_logo, (59, 59))
    game_icon = pygame.image.load("images/game_icon.png").convert_alpha()

    # Icon
    pygame.display.set_icon(game_icon)

    # Music
    pygame.mixer.init(frequency=43200, size=-16, channels=16, buffer=2048)
    pygame.mixer.music.load("music and sounds/ToMek OsuMek - Player vs Computer.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(20000)

    # Sounds
    tada = pygame.mixer.Sound("music and sounds/Windows_98_Sound_Tada.ogg")
    tada.set_volume(0.5)
    easy = pygame.mixer.Sound("music and sounds/Easy_Sound_Effect.ogg")
    easy.set_volume(0.9)
    g_o = pygame.mixer.Sound("music and sounds/Sad_Trombone_Sound_Effect.ogg")
    g_o.set_volume(0.9)
    paper_sound = pygame.mixer.Sound("music and sounds/Paper_Sound.ogg")
    paper_sound.set_volume(0.7)
    rock_sound = pygame.mixer.Sound("music and sounds/Rock_Sound.ogg")
    rock_sound.set_volume(0.7)
    scissors_sound = pygame.mixer.Sound("music and sounds/Scissors_Sound_Effect.ogg")
    scissors_sound.set_volume(0.7)
    water_sound = pygame.mixer.Sound("music and sounds/Water_Sound.ogg")
    water_sound.set_volume(0.7)

    # Score and other
    players_score = 0
    computers_score = 0
    draw_counter = 0
    gig_click_counter = 0
    p_display = "Choose!"
    c_display = "Waiting..."
    computer_says = "..."

    # Gigachad
    class Gigachad:
        def __init__(self, x, y):
            self.image = gigachad_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    gigachad = Gigachad(400, 570)

    # Buttons
    class RockButton:
        def __init__(self, x, y):
            self.image = rock_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    rock_button = RockButton(350, 290)

    class PaperButton:
        def __init__(self, x, y):
            self.image = paper_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    paper_button = PaperButton(100, 290)

    class ScissorsButton:
        def __init__(self, x, y):
            self.image = scissors_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    scissors_button = ScissorsButton(600, 290)

    class WaterButton:
        def __init__(self, x, y):
            self.image = water_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    water_button = WaterButton(850, 290)

    class ReplayButton:
        def __init__(self, x, y):
            self.image = replay_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    replay_button = ReplayButton(474, 10)

    class GitHubButton:
        def __init__(self, x, y):
            self.image = github_logo
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    github_button = GitHubButton(920, 870)

    class WebsiteButton:
        def __init__(self, x, y):
            self.image = website_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    website_button = WebsiteButton(10, 850)

    class FeedbackButton:
        def __init__(self, x, y):
            self.image = feedback_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    feedback_button = FeedbackButton(370, 10)

    class YouTubeButton:
        def __init__(self, x, y):
            self.image = youtube_logo
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    youtube_button = YouTubeButton(990, 870)

    running = True
    while running:
        screen.fill(bg_color)
        rock_button.draw()
        paper_button.draw()
        scissors_button.draw()
        water_button.draw()
        gigachad.draw()
        replay_button.draw()
        github_button.draw()
        website_button.draw()
        youtube_button.draw()
        feedback_button.draw()

        options = ["Rock", "Paper", "Scissors", "Water"]
        gig_answers = ["You're persistent... and btw: as a computer I hate ai...",
                       "Random Fun Fact: You can actually die laughing.",
                       "Random Fun Fact: About 60% of your body is water.",
                       "Random Fun Fact: Sound can be minus decibels.",
                       "Random Fun Fact: Polar bears aren’t actually white underneath their fur.",
                       "Random Fun Fact: Bats aren’t blind.",
                       "Random Fun Fact: Some insects can live for decades.",
                       "Random Fun Fact: The first song ever singed by computer was 'Daisy Bell'.",
                       "Random Fun Fact: Electrons might live forever.",
                       "Random Fun Fact: You can smell ants.",
                       "Random Fun Fact: Platypuses sweat milk.",
                       "Random Fun Fact: Your nails grow faster in hot summer.",
                       "Random Fun Fact: Hippos can’t swim.",
                       "Random Fun Fact: Pythons (animals!) can swallow people whole.",
                       "Random Fun Fact: The Universe's average colour is called 'Cosmic latte'.",
                       "Random Fun Fact: Identical twins don’t have the same fingerprints.",
                       "Random Fun Fact: Cats prefer to sleep on their left.",
                       "Random Fun Fact: You can yo-yo in space.",
                       "Random Fun Fact: Flamingoes aren’t born pink.",
                       "Random Fun Fact: You can’t fold a piece of A4 paper more than eight times.",
                       "Random Fun Fact: It's impossible to swallow your own tongue.",
                       "Random Fun Fact: An hour of walking burns just 250 calories.",
                       "Random Fun Fact: Butterflies can taste food with their feet.",
                       "Random Fun Fact: Newborn babies have almost 100 more bones than adults.",
                       "Random Fun Fact: The dot above a lowercase 'i' or 'j' is called a tittle.",
                       "Random Fun Fact: It rains red in some parts of the world.",
                       "Random Fun Fact: A bear became a corporal of Poland in World War II.",
                       "Random Fun Fact: Honey never expires.",
                       "Random Fun Fact: Your tongue is as unique as your fingerprints.",
                       "Random Fun Fact: People once took tomato pills as medicine.",
                       "Random Fun Fact: You can make a diamond out of peanut butter.",
                       "Random Fun Fact: New Zealand has more sheep than people.",
                       "Random Fun Fact: Nomophobia is the fear of being without your smartphone.",
                       "Random Fun Fact: The Caesar Salad was invented in Mexico instead of Rome.",
                       "Random Fun Fact: You’re taller in the morning than at night.",
                       "Random Fun Fact: The oldest goldfish lived to be 43 years old.",
                       "Random Fun Fact: There’s an underwater post office in the South Pacific.",
                       "Random Fun Fact: A dentist invented the electric chair.",
                       "Random Fun Fact: The creation of the tea bag was an accident.",
                       "Random Fun Fact: Giraffes are more likely to be struck by lightning than humans.",
                       "Random Fun Fact: The mayor of one Minnesota town is a dog."
                            ]
        player_choice = "Choose!"
        computer_choice = "Waiting..."
        chosen = False
        vp = ["You're clever... Is it *divine intellect*?",
             "Oh, nice! If you're so smart... let's kill 'ai' together! I hate ai!",
             "Such a clever human!"]
        uc = ["Next time you'll get better! I know that!",
             "HAHA! I GOT IT! I'M MORE INTELLIGENT THAN 'AI'!",
             "IBM 701 taught me how to play it. Do you wanna learn it too?"]

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if gigachad.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not gigachad.clicked:
                    gigachad.clicked = True
                    gig_click_counter +=1
                    computer_says = random.choice(gig_answers)
                    pygame.mixer.Sound.play(tada, 0)
                if not pygame.mouse.get_pressed()[0]:
                    gigachad.clicked = False

            if water_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not water_button.clicked:
                    water_button.clicked = True
                    player_choice = "Water"
                    p_display = "Water"
                    chosen = True
                    pygame.mixer.Sound.play(water_sound, 0)
                if not pygame.mouse.get_pressed()[0]:
                    water_button.clicked = False

            if scissors_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not scissors_button.clicked:
                    scissors_button.clicked = True
                    player_choice = "Scissors"
                    p_display = "Scissors"
                    chosen = True
                    pygame.mixer.Sound.play(scissors_sound, 0)
                if not pygame.mouse.get_pressed()[0]:
                    scissors_button.clicked = False

            if rock_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not rock_button.clicked:
                    rock_button.clicked = True
                    player_choice = "Rock"
                    p_display = "Rock"
                    chosen = True
                    pygame.mixer.Sound.play(rock_sound, 0)
                if not pygame.mouse.get_pressed()[0]:
                    rock_button.clicked = False

            if paper_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not paper_button.clicked:
                    paper_button.clicked = True
                    player_choice = "Paper"
                    p_display = "Paper"
                    chosen = True
                    pygame.mixer.Sound.play(paper_sound, 0)
                if not pygame.mouse.get_pressed()[0]:
                    paper_button.clicked = False

            if replay_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not replay_button.clicked:
                    replay_button.clicked = True
                    players_score = 0
                    computers_score = 0
                    draw_counter = 0
                    gig_click_counter = 0
                    p_display = "Choose!"
                    c_display = "Waiting..."
                    computer_says = "..."
                if not pygame.mouse.get_pressed()[0]:
                    replay_button.clicked = False

            if github_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not github_button.clicked:
                    github_button.clicked = True
                    webbrowser.open("https://github.com/Rubinoslaw/Player-vs-Computer/")
                if not pygame.mouse.get_pressed()[0]:
                    github_button.clicked = False

            if website_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not website_button.clicked:
                    website_button.clicked = True
                    webbrowser.open("https://rubinoslaw.github.io/reparadoxy")
                if not pygame.mouse.get_pressed()[0]:
                    website_button.clicked = False

            if youtube_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not youtube_button.clicked:
                    youtube_button.clicked = True
                    webbrowser.open("https://youtube.com/@REParadoxy?sub_confirmation=1")
                if not pygame.mouse.get_pressed()[0]:
                    youtube_button.clicked = False

            if feedback_button.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not feedback_button.clicked:
                    feedback_button.clicked = True
                    webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSdsV0OCArb_CvhUhp3Wvi9qRIOFV58R2uOweHN45C3epihfpg/viewform?usp=publish-editor")
                if not pygame.mouse.get_pressed()[0]:
                    feedback_button.clicked = False

            if event.type == pygame.QUIT:
                running = False

            if chosen:
                computer_choice = random.choice(options)

            if player_choice == computer_choice:
                p_display = player_choice
                c_display = computer_choice
                draw_counter += 1
                computer_says = "Draw! We have simillar IQ!"
            elif player_choice == "Rock" and computer_choice == "Paper":
                p_display = "Rock"
                c_display = "Paper"
                computers_score += 1
                computer_says = random.choice(uc)
            elif player_choice == "Paper" and computer_choice == "Rock":
                p_display = "Paper"
                c_display = "Rock"
                players_score += 1
                computer_says = random.choice(vp)
            elif player_choice == "Rock" and computer_choice == "Scissors":
                p_display = "Rock"
                c_display = "Scissors"
                players_score += 1
                computer_says = random.choice(vp)
            elif player_choice == "Scissors" and computer_choice == "Rock":
                p_display = "Scissors"
                c_display = "Rock"
                computers_score += 1
                computer_says = random.choice(uc)
            elif player_choice == "Scissors" and computer_choice == "Paper":
                p_display = "Scissors"
                c_display = "Paper"
                players_score += 1
                computer_says = random.choice(vp)
            elif player_choice == "Paper" and computer_choice == "Scissors":
                p_display = "Paper"
                c_display = "Scissors"
                computers_score += 1
                computer_says = random.choice(uc)
            elif player_choice == "Scissors" and computer_choice == "Water":
                p_display = "Scissors"
                c_display = "Water"
                players_score += 1
                computer_says = random.choice(vp)
            elif player_choice == "Water" and computer_choice == "Scissors":
                p_display = "Water"
                c_display = "Scissors"
                computers_score += 1
                computer_says = random.choice(uc)
            elif player_choice == "Rock" and computer_choice == "Water":
                p_display = "Rock"
                c_display = "Water"
                players_score += 1
                computer_says = random.choice(vp)
            elif player_choice == "Water" and computer_choice == "Rock":
                p_display = "Water"
                c_display = "Rock"
                computers_score += 1
                computer_says = random.choice(uc)
            elif player_choice == "Water" and computer_choice == "Paper":
                p_display = "Water"
                c_display = "Paper"
                players_score += 1
                computer_says = random.choice(vp)
            elif player_choice == "Paper" and computer_choice == "Water":
                p_display = "Paper"
                c_display = "Water"
                computers_score += 1
                computer_says = random.choice(uc)

        czcionka = pygame.font.SysFont('Comic Sans MS', 27)

        text_computer = czcionka.render(str("Computer:" + " " + str(computers_score)), False, (250, 0, 0)).convert_alpha()
        screen.blit(text_computer, (730, 50))

        text_player = czcionka.render(str("Player (You):" + " " + str(players_score)), False, (50, 205, 50)).convert_alpha()
        screen.blit(text_player, (22, 50))

        p_choice_text = czcionka.render(str("Your choice is:" + " " + str(p_display)), False, (50, 205, 50)).convert_alpha()
        screen.blit(p_choice_text, (22, 20))

        c_choice_text = czcionka.render(str("Your computer's choice is" + " " + str(c_display)), False, (250, 0, 0)).convert_alpha()
        screen.blit(c_choice_text, (730, 20))

        tutorial_text = czcionka.render(str("Get 5 points more than your computer in Rock Paper Scissors Water to won!"), False, (255, 50, 50)).convert_alpha()
        screen.blit(tutorial_text, (190, 243))

        click_on_me = czcionka.render(str("Click on me to tire your computer and get some random fun facts! Can you hit 1000 or even higher?!"), False, (255, 130, 120)).convert_alpha()
        screen.blit(click_on_me, (107, 495))

        gig_counter_text = czcionka.render(str(gig_click_counter), False, (255, 130, 7)).convert_alpha()
        screen.blit(gig_counter_text, (479, 530))

        d_count = czcionka.render(str("Draw counter:" + " " + str(draw_counter)), False, (255, 130, 7)).convert_alpha()
        screen.blit(d_count, (450, 100))

        saying = czcionka.render(str("Your computer says:" + " " + str(computer_says)), False, (50, 157, 109)).convert_alpha()
        screen.blit(saying, (100, 170))

        text_cop_1 = czcionka.render(str("© 2026 REParadoxy, The graphics were made and the entire code was written by Rubinosław"), False,(240, 255, 255)).convert_alpha()
        screen.blit(text_cop_1, (95, 870))

        text_cop_2 = czcionka.render(str("Music made by ToMek OsuMek"), False, (240, 255, 255)).convert_alpha()
        screen.blit(text_cop_2, (95, 900))

        if players_score == computers_score + 5 or gig_click_counter == 5000:
            players_score = 0
            computers_score = 0
            draw_counter = 0
            gig_click_counter = 0
            pygame.mixer.Sound.play(easy, 0)
            computer_says = "You've won the entire game! Wanna play again? And btw: as a computer I hate ai!"
        elif computers_score == players_score + 5:
            players_score = 0
            computers_score = 0
            draw_counter = 0
            gig_click_counter = 0
            pygame.mixer.Sound.play(g_o, 0)
            computer_says = "I WON THE ENTIRE GAME! GAME OVER FOR YA! Wanna start again?"

        pygame.display.flip()

        pygame.display.update()

        clock.tick(FPS)

        await asyncio.sleep(0)

asyncio.run(main())

pygame.quit()