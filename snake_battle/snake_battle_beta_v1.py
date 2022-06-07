
def game_over(Loser, winner, red, frame_size_x, frame_size_y, game_window, black): #此function功能為繪製遊戲結束畫面(有玩家自殺)
    my_font = pygame.font.SysFont('times new roman', 48)
    my_font2 = pygame.font.SysFont('times new roman', 36)
    game_over_surface = my_font.render('Game over ! Suicide is Not the answer. Press Esc to leave', True, red) #.render => 畫字體
    game_over_surface2 = my_font2.render('Winner is : '+ winner, True, red)
    game_over_rect = game_over_surface.get_rect() #返回矩形大小，下列為位置
    #attribute =x, y, top, left, bottom, right, topleft, bottomleft, topright, bottomright, midtop, midleft, midbottom, midright, center, centerx, centery, size, width, height, w, h
    game_over_rect2 = game_over_surface2.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_over_rect2.midtop = (frame_size_x/2, frame_size_y/3+100)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_surface2, game_over_rect2)
    pygame.display.flip()
    time.sleep(1)
    return 1

def next_stage(winner, red, frame_size_x, frame_size_y, game_window, black):  #繪製下一關前過場畫面(有玩家達成全目標掠食)
    my_font = pygame.font.SysFont('times new roman', 90)
    my_font2 = pygame.font.SysFont('times new roman', 36)
    game_over_surface = my_font.render('Press SPACE To Next Stage', True, red) #.render => 畫字體
    game_over_surface2 = my_font2.render('winner is : '+ winner, True, red)
    game_over_rect = game_over_surface.get_rect() #返回矩形大小
    #attribute =x, y, top, left, bottom, right, topleft, bottomleft, topright, bottomright, midtop, midleft, midbottom, midright, center, centerx, centery, size, width, height, w, h
    game_over_rect2 = game_over_surface2.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_over_rect2.midtop = (frame_size_x/2, frame_size_y/3+100)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_surface2, game_over_rect2)
    
    pygame.display.flip()
    time.sleep(1)
    return 1, winner

def conti(stage, winner): #指示執行下一關的function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #print('you press pause')
                print('stage=', stage)
                main(stage, winner) #傳遞關卡與贏家參數

def end():
    """
    按X關掉程式 and 按ESC關掉程式!
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('Quit')
                pygame.quit()
                sys.exit()

def final_scene(winner, red, frame_size_x, frame_size_y, game_window, black): #繪製通關畫面
    my_font = pygame.font.SysFont('times new roman', 48)
    my_font2 = pygame.font.SysFont('times new roman', 36)
    game_over_surface = my_font.render('Thanks for playing Snake Battle beta1.0', True, red) #.render => 畫字體
    game_over_surface2 = my_font2.render('Winner is : '+ winner, True, red)
    game_over_rect = game_over_surface.get_rect() #返回矩形大小
    #attribute =x, y, top, left, bottom, right, topleft, bottomleft, topright, bottomright, midtop, midleft, midbottom, midright, center, centerx, centery, size, width, height, w, h
    game_over_rect2 = game_over_surface2.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_over_rect2.midtop = (frame_size_x/2, frame_size_y/3+100)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_surface2, game_over_rect2)
    pygame.display.flip()
    time.sleep(1)
    return 1

# Main logic <主程式邏輯>
def main(stage=1, winner=None):

    # Initialize pygame and check for errors encountered
    check_errors = pygame.init()
    if check_errors[1] > 0:
        #print('Had {} errors when initialising game, exiting...'.format(check_errors[1]))
        sys.exit(-1)

    pygame.mixer.music.load('./game_music.mp3') #載入遊戲音樂
    pygame.mixer.music.play(loops=100, start=0.0) #播放遊戲音樂
    # 設定程式視窗大小為1290*640，設定程式標題為Snake
    frame_size_x = 1290 #一邊為640 boundary = 10
    frame_size_y = 640
    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    pygame.display.set_caption('Snake_battle')
    central_bourder = frame_size_x / 2

    # Game variables
    # Colors (R, G, B)
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    snake_head = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]  #snake1起始位置

    snake2_head = [1190, 50]
    snake2_body = [[1190, 50], [1190+10, 50], [1190+(2*10), 50]] #snake2起始位置

#以下以if 判定進入關卡1~5
    if stage == 1:
        #print('winner=',winner)
        food_pos_list = []
        food_pos_for2_list = []
        clear = 3 #目標點數量設置
        clear_2 = 3
        for i in range(3):
            food_x_for1 = random.randrange(1, (central_bourder //10 -1)) * 10  #計算food座標
            food_y_for1 = random.randrange(1, (frame_size_y//10)) * 10
            food_pos = [food_x_for1, food_y_for1]
            food_pos_list.append(food_pos)
            food_spawn = True

            food_x_for2 = random.randrange((central_bourder //10 + 1), frame_size_x//10) * 10 #計算food(for snake2)座標
            food_y_for2 = random.randrange(1, (frame_size_y//10)) * 10
            food_pos_for2 = [food_x_for2, food_y_for2]
            food_pos_for2_list.append(food_pos_for2)
            food_spawn_2 = True

    if stage == 2:
        if winner == "player1": #贏家輸家進入下關起始長度不同，傳遞winner參數再用if分別處理
            #print('winner=',winner)
            snake_head = [100+30, 50]
            snake_body = [[100+30, 50], [100-10+30, 50], [100-(2*10)+30, 50]]
            for i in range(3):
                snake_body.append([100-(i*10), 50])
            food_pos_list = []
            food_pos_for2_list = []
            clear = 5
            clear_2 = 5
            for i in range(5): 
                food_x_for1 = random.randrange(1, (central_bourder //10 -1)) * 10
                food_y_for1 = random.randrange(1, (frame_size_y//10)) * 10
                food_pos = [food_x_for1, food_y_for1]
                food_pos_list.append(food_pos)
                food_spawn = True

                food_x_for2 = random.randrange((central_bourder //10 + 4), (frame_size_x//10) - 3) * 10 #平衡難度，輸家在下關有隱藏優勢，目標點生成範圍將縮小一些
                food_y_for2 = random.randrange(4, (frame_size_y//10)-3) * 10
                food_pos_for2 = [food_x_for2, food_y_for2]
                food_pos_for2_list.append(food_pos_for2)
                food_spawn_2 = True
        else:
            #print('winner=',winner)
            snake2_head = [1190-30, 50]
            snake2_body = [[1190-30, 50], [1190+10-30, 50], [1190+(2*10)-30, 50]]
            for i in range(3):
                snake2_body.append([1190+(i*10), 50])
            food_pos_list = []
            food_pos_for2_list = []
            clear = 5
            clear_2 = 5
            for i in range(5):
                food_x_for1 = random.randrange(4, (central_bourder //10 -4)) * 10
                food_y_for1 = random.randrange(4, (frame_size_y//10)-4) * 10
                food_pos = [food_x_for1, food_y_for1]
                food_pos_list.append(food_pos)
                food_spawn = True

                food_x_for2 = random.randrange((central_bourder //10 + 1), frame_size_x//10) * 10
                food_y_for2 = random.randrange(1, (frame_size_y//10)) * 10
                food_pos_for2 = [food_x_for2, food_y_for2]
                food_pos_for2_list.append(food_pos_for2)
                food_spawn_2 = True
                
    if stage == 3:
        if winner == "player1":
            #print('winner=',winner)
            snake_head = [100+70, 50]
            snake_body = [[100+70, 50], [100-10+70, 50], [100-(2*10)+70, 50]]
            for i in range(7):
                snake_body.append([100-(i*10)+40, 50])
            food_pos_list = []
            food_pos_for2_list = []
            clear = 7
            clear_2 = 7
            for i in range(7):
                food_x_for1 = random.randrange(1, (central_bourder //10 -1)) * 10
                food_y_for1 = random.randrange(1, (frame_size_y//10)) * 10
                food_pos = [food_x_for1, food_y_for1]
                food_pos_list.append(food_pos)
                food_spawn = True

                food_x_for2 = random.randrange((central_bourder //10 + 8), (frame_size_x//10) - 7) * 10
                food_y_for2 = random.randrange(8, (frame_size_y//10)-7) * 10
                food_pos_for2 = [food_x_for2, food_y_for2]
                food_pos_for2_list.append(food_pos_for2)
                food_spawn_2 = True
        else:
           #print('winner=',winner)
            snake2_head = [1190-70, 50]
            snake2_body = [[1190-70, 50], [1190+10-70, 50], [1190+(2*10)-70, 50]]
            for i in range(7):
                snake2_body.append([1190+(i*10)-40, 50])
            food_pos_list = []
            food_pos_for2_list = []
            clear = 7
            clear_2 = 7
            for i in range(7):
                food_x_for1 = random.randrange(8, (central_bourder //10 -8)) * 10
                food_y_for1 = random.randrange(8, (frame_size_y//10)-8) * 10
                food_pos = [food_x_for1, food_y_for1]
                food_pos_list.append(food_pos)
                food_spawn = True

                food_x_for2 = random.randrange((central_bourder //10 + 1), frame_size_x//10) * 10
                food_y_for2 = random.randrange(1, (frame_size_y//10)) * 10
                food_pos_for2 = [food_x_for2, food_y_for2]
                food_pos_for2_list.append(food_pos_for2)
                food_spawn_2 = True

    if stage == 4:
        if winner == "player1":
            #print('winner=',winner)
            snake_head = [100+110, 50]
            snake_body = [[100+110, 50], [100-10+110, 50], [100-(2*10)+110, 50]]
            for i in range(11):
                snake_body.append([100-(i*10)+90, 50])
            food_pos_list = []
            food_pos_for2_list = []
            clear = 11
            clear_2 = 11
            for i in range(11):
                food_x_for1 = random.randrange(1, (central_bourder //10 -1)) * 10
                food_y_for1 = random.randrange(1, (frame_size_y//10)) * 10
                food_pos = [food_x_for1, food_y_for1]
                food_pos_list.append(food_pos)
                food_spawn = True

                food_x_for2 = random.randrange((central_bourder //10 + 12), (frame_size_x//10) - 11) * 10
                food_y_for2 = random.randrange(12, (frame_size_y//10)-11) * 10
                food_pos_for2 = [food_x_for2, food_y_for2]
                food_pos_for2_list.append(food_pos_for2)
                food_spawn_2 = True
        else:
            #print('winner=',winner)
            snake2_head = [1190-110, 50]
            snake2_body = [[1190-110, 50], [1190+10-110, 50], [1190+(2*10)-110, 50]]
            for i in range(11):
                snake2_body.append([1190+(i*10)-90, 50])
            food_pos_list = []
            food_pos_for2_list = []
            clear = 11
            clear_2 = 11
            for i in range(11):
                food_x_for1 = random.randrange(12, (central_bourder //10 -12)) * 10
                food_y_for1 = random.randrange(12, (frame_size_y//10)-12) * 10
                food_pos = [food_x_for1, food_y_for1]
                food_pos_list.append(food_pos)
                food_spawn = True

                food_x_for2 = random.randrange((central_bourder //10 + 1), frame_size_x//10) * 10
                food_y_for2 = random.randrange(1, (frame_size_y//10)) * 10
                food_pos_for2 = [food_x_for2, food_y_for2]
                food_pos_for2_list.append(food_pos_for2)
                food_spawn_2 = True

    if stage == 5:
        #print('winner=',winner)
        snake_head = [100+130, 50]
        snake_body = [[100+130, 50], [100-10+130, 50], [100-(2*10)+130, 50]]
        snake2_head = [1190-110, 50]
        snake2_body = [[1190-110, 50], [1190+10-110, 50], [1190+(2*10)-110, 50]]
        for i in range(13):
            snake_body.append([100-(i*10)+110, 50])
        for i in range(13):
            snake2_body.append([1190+(i*10)-110, 50])
        food_pos_list = []
        food_pos_for2_list = []
        clear = 25
        clear_2 = 25
        for i in range(25):
            food_x_for1 = random.randrange(1, (central_bourder //10 -1)) * 10
            food_y_for1 = random.randrange(1, (frame_size_y//10)) * 10
            food_pos = [food_x_for1, food_y_for1]
            food_pos_list.append(food_pos)
            food_spawn = True

            food_x_for2 = random.randrange((central_bourder //10 + 1), frame_size_x//10) * 10
            food_y_for2 = random.randrange(1, (frame_size_y//10)) * 10
            food_pos_for2 = [food_x_for2, food_y_for2]
            food_pos_for2_list.append(food_pos_for2)
            food_spawn_2 = True
    
    change_to = direction = 'RIGHT'
    snake2_change_to = direction_2 = 'LEFT'

    over = 0

    count_for_1 = 0
    count_for_2 = 0
    while True: #迴圈開始
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:

                # W -> Up; S -> Down; A -> Left; D -> Right 控制左邊 #方向鍵上下左右 控制右邊
                if event.key == pygame.K_UP:
                    snake2_change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    snake2_change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    snake2_change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    snake2_change_to = 'RIGHT'
                if event.key == ord('w'):
                    change_to = 'UP'
                if event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == ord('d'):
                    change_to = 'RIGHT'
            

                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))


        # 當按下方向鍵上下左右時，蛇行進方向會依據指令改變，但不會下變上，左變右這種變化。
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        if snake2_change_to == 'UP' and direction_2 != 'DOWN':
            direction_2 = 'UP'
        if snake2_change_to == 'DOWN' and direction_2 != 'UP':
            direction_2 = 'DOWN'
        if snake2_change_to == 'LEFT' and direction_2 != 'RIGHT':
            direction_2 = 'LEFT'
        if snake2_change_to == 'RIGHT' and direction_2 != 'LEFT':
            direction_2 = 'RIGHT'

    
        # 行進時snake head座標根據指令改變 每次移動10 pixel
        if direction == 'UP':
            snake_head[1] -= 10
        if direction == 'DOWN':
            snake_head[1] += 10
        if direction == 'LEFT':
            snake_head[0] -= 10
        if direction == 'RIGHT':
            snake_head[0] += 10
        if direction_2 == 'UP':
            snake2_head[1] -= 10
        if direction_2 == 'DOWN':
            snake2_head[1] += 10
        if direction_2 == 'LEFT':
            snake2_head[0] -= 10
        if direction_2 == 'RIGHT':
            snake2_head[0] += 10


        # 當蛇吃到食物時(head座標==食物座標)，score += 1，且snake body會接在head。吃到後food_spawn = false。else中設計巧妙，如果沒吃到東西會把snakebody中head踢掉，而有吃到東西的話才會保留，因此蛇長度會加長!
        snake_body.insert(0, list(snake_head))
        snake2_body.insert(0, list(snake2_head))
        #print('snake_head=',snake_head)
        #print('snake_body=',snake_body)
        afterclear = clear
        for food_pos in food_pos_list:
            if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
                #score += 1
                food_spawn = False
                afterclear = clear - 1
                food_pos_list.remove(food_pos)
                count_for_1 += 1
        if afterclear == clear:          
            snake_body.pop()
            #print('snake_body=',snake_body)
            
        afterclear_2 = clear_2 #snake2吃到食物
        for food_pos_for2 in food_pos_for2_list:
            if snake2_head[0] == food_pos_for2[0] and snake2_head[1] == food_pos_for2[1]:
                #score2 += 1
                food_spawn_2 = False
                afterclear_2 = clear_2 - 1
                food_pos_for2_list.remove(food_pos_for2)
                count_for_2 += 1
        if afterclear_2 == clear_2:
            snake2_body.pop()
            #print('snake_body=',snake_body2)

        # Spawning food on the screen
        if count_for_1 == clear: #當吃到的目標點等於該關卡的目標則進入下一關
            win = 1
            if stage == 5:
                #print('666')
                over=final_scene('player1', red, frame_size_x, frame_size_y, game_window, black)
                if over == 1:
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
            over, winner = next_stage('player1', red, frame_size_x, frame_size_y, game_window, black)
            snake_head[0] = central_bourder
            snake_head[1] = frame_size_y / 2
            snake2_head[0] = central_bourder
            snake2_head[1] = frame_size_y / 2
            conti(stage+1, winner)
            
        if count_for_2 == clear_2: #當snake2吃到的目標點等於該關卡的目標則進入下一關
            win = 2
            if stage == 5:
                #print('666')
                over=final_scene('player2', red, frame_size_x, frame_size_y, game_window, black)
                if over == 1:
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
            over, winner = next_stage('player2', red, frame_size_x, frame_size_y, game_window, black)
            snake_head[0] = central_bourder
            snake_head[1] = frame_size_y / 2
            snake2_head[0] = central_bourder
            snake2_head[1] = frame_size_y / 2
            conti(stage+1, winner)
            #over = 1

        # Display
        game_window.fill(white)
        bg = pygame.image.load("./bg.png")
        game_window.blit(bg, (0, 0))

        # Draw Snake
        for pos in snake_body:
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            #print(pos)
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        for pos in snake2_body:
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            #print(pos)
            pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))

        # Draw food
        for food_pos in food_pos_list:
            pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
            myimage = pygame.image.load("frog2.png") #青蛙影像
            myimage = pygame.transform.scale(myimage,(36,36))
            imagerect = myimage.get_rect()
            game_window.blit(myimage ,(food_pos[0], food_pos[1]))


        for food_pos_for2 in food_pos_for2_list:
            pygame.draw.rect(game_window, red, pygame.Rect(food_pos_for2[0], food_pos_for2[1], 10, 10))
            myimage = pygame.image.load("frog2.png")
            myimage = pygame.transform.scale(myimage,(36,36))
            imagerect = myimage.get_rect()
            game_window.blit(myimage ,(food_pos_for2[0], food_pos_for2[1]))


        # 碰到牆壁就game over，需要控制兩隻蛇的位置，以免其中一隻停了另一隻還移動。
        pygame.draw.rect(game_window, black, pygame.Rect(central_bourder, 0, 10, 640))

        if snake_head[0] < 0 or snake_head[0] > central_bourder:
            #over = game_over()
            #print(1)
            over=game_over('player1','player2', red, frame_size_x, frame_size_y, game_window, black)
            snake2_head[0] = central_bourder
            snake2_head[1] = frame_size_y / 2
            end()
        if snake_head[1] < 0 or snake_head[1] > frame_size_y-10:
            #over = game_over()
            #print(2)
            over=game_over('player1','player2', red, frame_size_x, frame_size_y, game_window, black)
            snake2_head[0] = central_bourder
            snake2_head[1] = frame_size_y / 2
            end()
        if snake2_head[0] > frame_size_x or snake2_head[0] < central_bourder:
            #over = game_over()
            #print('snake2_head= ',snake2_head)
            #print(frame_size_x)
            #print(central_bourder)
            #print(3)
            over=game_over('player2','player1', red, frame_size_x, frame_size_y, game_window, black)
            snake_head[0] = central_bourder
            snake_head[1] = frame_size_y / 2
            end()
        if snake2_head[1] < 0 or snake2_head[1] > frame_size_y-10:
            #over = game_over()
            #print('snake2_head= ',snake2_head)
            #print(frame_size_x)
            #print(central_bourder)
            #print(4)
            over=game_over('player2','player1', red, frame_size_x, frame_size_y, game_window, black)
            snake_head[0] = central_bourder-100
            snake_head[1] = frame_size_y / 2
            end()
        # 碰到自己就game over
        for block in snake_body[1:]:
            #print(block)
            #print(snake_head[0])
            if snake_head[0] == block[0] and snake_head[1] == block[1]:
                #over = game_over()
                #print(5)
                over=game_over('player1','player2', red, frame_size_x, frame_size_y, game_window, black)
                if over == 1:
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
        
        for block in snake2_body[1:]:
            #print('snake2_body=',snake2_body)
            #print(block)
            #print(snake2_head[0])
            if snake2_head[0] == block[0] and snake2_head[1] == block[1]:
                #over = game_over()
                #print(6)
                over=game_over('player2','player1', red, frame_size_x, frame_size_y, game_window, black)
                if over == 1:
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
        
        if not over:
            #show_score(1, white, 'consolas', 10)
            # Refresh game screen
            pygame.display.update()
            # Refresh rate
            if stage == 1:
                pygame.time.Clock().tick(40)
            elif stage == 2:
                pygame.time.Clock().tick(50)
            elif stage == 3:
                pygame.time.Clock().tick(60)
            elif stage == 4:
                pygame.time.Clock().tick(70)
            elif stage == 5:
                pygame.time.Clock().tick(80)

import pygame, sys, time, random            
main()
