# class Character:
#     """
#     모든 캐릭터의 모체가 되는 클래스
#     """

#     def __init__(self, name, hp, power):
#         self.name = name
#         self.max_hp = hp
#         self.hp = hp
#         self.power = power

#     def attack(self, other):
#         damage = random.randint(self.power - 2, self.power + 2)
#         other.hp = max(other.hp - damage, 0)
#         print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
#         if other.hp == 0:
#             print(f"{other.name}이(가) 쓰러졌습니다.")

#     def show_status(self):
#         print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


import random

# 플레이어와 몬스터의 공통 클래스(이름, hp, normal_power)


class BaseCharacter:
    def __init__(self, name, hp, mp, normal_power):
        self.name = name
        self.hp = hp
        # self.current_hp = hp
        self.mp = mp
        # self.current_mp = mp
        self.normal_power = normal_power

    # 공통 일반공격
    def normal_attack(self, target):
        normal_damage = random.randint(
            int(self.normal_power - 2), int(self.normal_power + 2))
        target.hp -= normal_damage
        print(f"{self.name}이(가) {target.name}에게 일반공격으로 {normal_damage}의 데미지를 입혔습니다.")

    # 상태창 표기
    def show_status(self):
        # self.current_hp = self.max_hp - 데미지...
        print(
            f"{self.name}의 체력은 {self.hp}입니다")


class Player(BaseCharacter):
    def __init__(self, name, hp, mp,
                 normal_power, magic_power):
        super().__init__(name, hp, mp, normal_power)
        print(self.name)
        self.hp = hp
        # self.max_hp = hp
        # self.current_hp = hp
        self.mp = mp
        # self.current_mp = mp
        self.magic_power = magic_power
        self.type_ = "인간"

    def magic_attack(self, target):
        magic_damage = random.randint(
            self.magic_power * 0.8, self.magic_power * 1.2)
        # 마나소모량20 추가하기 ,mp제한 미구현..
        self.mp -= 20
        target.hp -= magic_damage
        print(
            f"{self.type_} {self.name}이(가) {target.name}에게 마법으로 {magic_damage}의 데미지를 주었습니다. mp:{self.mp}")
        self.show_status()
        target.show_status()


class Monster(BaseCharacter):
    def __init__(self, name, hp, mp,
                 normal_power, magic_power):
        super().__init__(name, hp, mp, normal_power)
        self.name = name
        self.hp = hp
        self.mp = mp
        # self.max_mp = mp
        # self.current_mp = mp
        self.magic_power = magic_power
        self.type_ = "몬스터"

    def attack(self, target):
        attack_type = random.choice(["일반공격", "마법공격"])
        if attack_type == "일반공격":
            normal_damage = random.randint(
                int(self.normal_power - 2), int(self.normal_power + 2))
            target.hp -= normal_damage
            print(f"{self.name}이 {target.name}에게 일반공격으로 {normal_damage}의 데미지를 입혔습니다.")
        elif attack_type == "마법공격":
            magic_damage = random.randint(
                int(self.magic_power - 2), int(self.magic_power + 2))
            target.hp -= magic_damage
            self.mp -= 20
            print(f"{self.name}이 {target.name}에게 마법공격으로 {magic_damage}의 데미지를 입혔습니다.")


# 사용자 player_name을 input을 받은 후 player인스턴스 생성
player_name = input("플레이어 이름을 입력하세요: ")
player = Player(player_name, 150, 100, 20, 30)
monster = Monster("슬라임", 100, 60, 20, 20)


# while True:
while player.hp > 0 and monster.hp > 0:
    # show_status로 플레이어와 몬스터의 상태정보 출력
    print("\n")
    player.show_status()
    monster.show_status()
    print("\n\n")
    print("\n")
    if player.hp > 0:

        # exit이 입력되면 프로그램 종료
        print("일반공격은 1 을 입력, 마법공격은 2 를 입력,exit는 그만하기")
        action = input(": ")
        if action == "exit":
            print(f"{player_name}님이 도망치셨습니다.")
            break
        # 1번을 입력받을 경우 일반 공격
        elif action == "1":
            player.normal_attack(monster)
            if monster.hp > 0:
                monster.attack(player)
        # 2번을 입력받을 경우 마법 공격
        elif action == "2":
            player.magic_attack(monster)
            if monster.hp > 0:
                monster.attack(player)
        # 잘못 된 값이 입력 될 경우 경고 메세지를 출력하고 다시 입력받음
        else:
            print("잘못된 값이 입력됐습니다!")
            continue
if monster.hp <= 0:
    print(f"{player.name}께서 승리하셨습니다. 집에가자")
else:
    print(f"{monster.name}에게 져버렸다리")
