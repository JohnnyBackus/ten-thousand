# Prompt Documentation

We are instructed to use the AI platform of our choice to generate code for this lab and practice prompting.

## Approach

*Discussed approach with lab partner Kyle.*
[GameLogi whiteboard](ten_thousand/gamelogic.pdf)

## Prompt used to generate code

Create a class in python called GameLogic. This class will have two static methods. The first method is called "calculate_score" and the second method is called "roll_dice"

## Code received from AI

```import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_values):
        """
        Calculate the score based on the given dice values.

        Parameters:
        - dice_values (list): A list of integers representing the values of rolled dice.

        Returns:
        - int: The calculated score.
        """
        # Your scoring logic here
        score = sum(dice_values)  # Example: Sum of all dice values
        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Simulate rolling a specified number of dice.

        Parameters:
        - num_dice (int): The number of dice to roll.

        Returns:
        - list: A list of random integers representing the values of rolled dice.
        """
        # Your dice rolling logic here
        dice_values = [random.randint(1, 6) for _ in range(num_dice)]  # Example: Rolling a six-sided die
        return dice_values

# Example usage:
dice_values = GameLogic.roll_dice(3)
score = GameLogic.calculate_score(dice_values)
print(f"Dice values: {dice_values}")
print(f"Calculated score: {score}") 
```

## Subsequent Prompts
[ChatGPT Chat](https://chat.openai.com/share/d3fdceeb-9e1d-4633-9ece-04e72d6ef6e9)
*Multiple additional prompts used with mixed results.*
