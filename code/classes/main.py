# Do not modify these lines
__winc_id__ = "04da020dedb24d42adf41382a231b1ed"
__human_name__ = "classes"

# Add your code after this line

# =====================
#   Exercise: Classes
# =====================

# Part 1: Players
# ----------------
class Player:
    def __init__(self, name: str, speed: float, endurance: float, accuracy: float):
        self.name = name
        float_list = {"speed": speed, "endurance": endurance, "accuracy": accuracy}
        for key, value in float_list.items():
            if value <= 0 or value > 1:
                raise ValueError(f"{key} has to be a value from 0 up to 1 !")
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        highest = max(self.speed, self.endurance, self.accuracy)
        strength_dict = {"speed": self.speed, "endurance": self.endurance, "accuracy": self.accuracy}
        for key, value in strength_dict.items():
            if value == highest:
                return (key, value)


# Part 2: Commentators
# ---------------------
class Commentator:
    def __init__(self, name: str):
        self.name = name

    def sum_player(self, player_instance: object):
        return (
            getattr(player_instance, "speed")
            + getattr(player_instance, "endurance")
            + getattr(player_instance, "accuracy")
        )

    def compare_players(self, player1: object, player2: object, category: str):
        player_name1 = getattr(player1, "name")
        player_name2 = getattr(player2, "name")
        # Is one player better in this category as the other
        if getattr(player1, category) > getattr(player2, category):
            return player_name1
        elif getattr(player1, category) < getattr(player2, category):
            return player_name2
        # Players have equal scores, so comparing their strength
        strength1 = player1.strength()
        strength2 = player2.strength()
        if strength1[1] > strength2[1]:
            return player_name1
        elif strength1[1] < strength2[1]:
            return player_name2
        # Players have equal scores and equal strength, so compare their totals.
        if self.sum_player(player1) > self.sum_player(player2):
            return player_name1
        elif self.sum_player(player1) < self.sum_player(player2):
            return player_name2
        else:
            return "These two players might as well be twins!"
