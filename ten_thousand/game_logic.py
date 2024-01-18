import random
from collections import Counter

#score_table placed here for easy reference
score_table = (((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 3000),
        ((1, 1, 1, 1, 1, 1), 4000),
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 600),
        ((2, 2, 2, 2, 2, 2), 800),
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 900),
        ((3, 3, 3, 3, 3, 3), 1200),
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1200),
        ((4, 4, 4, 4, 4, 4), 1600),
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 1500),
        ((5, 5, 5, 5, 5, 5), 2000),
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 1800),
        ((6, 6, 6, 6, 6, 6), 2400),
        ((1, 2, 3, 4, 5, 6), 1500),
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
        ((1, 1, 1, 2, 2, 2), 1200))

class GameLogic:

    def __init__(self, name="forkle, not farkle"):
        self.name = name

    @staticmethod
    def calculate_score(dice_values):
        score = 0

        """
        Parameters:
        - dice_values (list): A list of integers representing the values of rolled dice.

        Returns:
        - int: The calculated score based on the score table and rolled dice values.
        """
     
        # Count occurrences of each dice value
        # Cumulate score based on score table
        print("dice_values: ", dice_values)
        
        # test for straight
        sorted_dice_values = sorted(dice_values)
        if sorted_dice_values == [1,2,3,4,5,6]:
            score += 1500
            return score # exit function
        
        # test for three pairs
        if len(Counter(dice_values)) == 3 and Counter(dice_values).most_common(1)[0][1] == 2:
            score += 1500
            return score # exit function
        
        # scores for 1's and 5's are special cases
        if dice_values.count(1) < 7 and dice_values.count(1) > 2:
            score += 1000 * (dice_values.count(1) - 2)
        else:
            score += 100 * dice_values.count(1)

        if dice_values.count(5) < 7 and dice_values.count(5) > 2:
            score += 500 * (dice_values.count(5) - 2)
        else:
            score += 50 * dice_values.count(5)

        # scores for 2, 3, 4, 6 follow the same pattern
        if dice_values.count(2) > 2:
            score += 200 * (dice_values.count(2) - 2)
        if dice_values.count(3) > 2:
            score += 300 * (dice_values.count(3) - 2)
        if dice_values.count(4) > 2:
            score += 400 * (dice_values.count(4) - 2)
        if dice_values.count(6) > 2:
            score += 600 * (dice_values.count(6) - 2)

        return score

    @staticmethod
    def roll_dice(num_dice = 6):
        """
        Simulate rolling a specified number of dice.

        Parameters:
        - num_dice (int): the number of dice to roll.

        Returns:
        - tuple of random integers representing the values of rolled dice.
        """
        dice_values = []
        print("Rolling", num_dice, "dice...")
        for _ in range(num_dice):
            dice_values.append(random.randint(1, 6))  # Example: Rolling a six-sided die
        print("***", dice_values, "***")
        return tuple(dice_values)
    


# Example usage:
# print("roll_dice: ", GameLogic.roll_dice(6))
# print("calculate_score: ", GameLogic.calculate_score((1,2,3,3,4,6)))



# def main():
#     if __name__ == "__main__":
#     main()