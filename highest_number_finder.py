

class HighestNumberFinder:
    def find_highest_number(self, numbers):
        if len(numbers) < 1:
            raise Exception
        return max(numbers)