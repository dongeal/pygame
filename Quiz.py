import pygame 
import random
###################################################
# 기본 초기화 부분
pygame.init() # 초기화(반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로
screen_height = 640  #세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz") #게임 이름

# FPS
clock = pygame.time.Clock()
###################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지,좌표, 속도, 폰트 등)
# 배경 만들기
background = pygame.image.load("background.png")

#캐릭터 (스프라이트) 불러오기
character = pygame.image.load("dog.png")
character_size =  character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 중앙
character_y_pos = screen_height - character_height # 화면 의 가장 아래

# 이동할 좌표
to_x = 0


# 캐릭터 이동 속도
character_speed = 0.6

# 적군 불러오기
enemy = pygame.image.load("ddong.png")
enemy_size =  enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos = random.randint(0,screen_width - enemy_width) # 랜덤 x
enemy_y_pos = 0 # 화면 맨위
enemy_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN: # 키가 눌렸는지 확이
            if event.key ==  pygame.K_LEFT: # 캐릭터를 왼쪽으로 
                to_x -= character_speed
            elif event.key ==  pygame.K_RIGHT: # 캐릭터를 오른쪽으로 
                to_x += character_speed
        
        if event.type == pygame.KEYUP: # 방향키 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            
            
    # 3. 게임 캐릭터 위치정의
    character_x_pos += to_x * dt

    #가로 경계값
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos >= screen_height:
        enemy_x_pos = random.randint(0,screen_width - enemy_width) # 랜덤 x
        enemy_y_pos = 0 # 화면 맨위

    # 4. 충돌처리 
    # 충돌처리 룰 위한 rect 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기
    
    screen.blit(enemy,(enemy_x_pos , enemy_y_pos)) # 적 그리기

    
    pygame.display.update()
  
    


pygame.quit()