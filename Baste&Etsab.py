class LotteryGame:
    """Handles the logic for the lottery game, comparing player numbers with winning numbers."""
    
    def __init__(self, winning_numbers, player_card):
        self.winning_set = set(winning_numbers)
        self.player_set = set(player_card)
        
        self.prize_map = {
            1: 1000,
            3: 3000,
            6: 1000000
        }

    def check_prizes(self, player_name="Player"):
        """Method to check the number of matching numbers and calculate prize."""
        
        matches = self.winning_set.intersection(self.player_set)
        num_matches = len(matches)
        
        winnings = self.prize_map.get(num_matches, 0)
        
        if winnings > 0:
            win_status = f"You won {winnings:,} pesos!"
        else:
            win_status = "No match!"
        
        print(f"\n{player_name}'s card: {sorted(list(self.player_set))}")
        print(f"Winning numbers: {sorted(list(self.winning_set))}")
        print(f"Has {num_matches} matched number(s) {sorted(list(matches))}. {win_status}")


# =========================================================
# Main Execution / Demonstration (OOP)
# =========================================================
class OOPDemo:
    """A class that demonstrates the use of all the above classes."""
    
    def __init__(self):
        self.grading_system = GradingSystem()
        self.lottery_game = None  # To be initialized later

    def run_flames_demo(self):
        print("\n--- 1. FLAMES Game ---")
        game1 = SimpleMatingGame("Thailang Nabuyuki", "Alice Eng")
        game1.display_result()
    
    def run_grading_system_demo(self):
        print("\n--- 2. Grading System (Interactive) ---")
        self.grading_system.input_grades()
        self.grading_system.display_results()

    def run_lottery_game_demo(self):
        print("\n--- 3. Lottery Game ---")
        winning_numbers = [12, 36, 18, 59, 26, 54]
        
        # Player A with 3 matches
        player_a_card = [23, 58, 26, 40, 36, 12]
        player_a_lotto = LotteryGame(winning_numbers, player_a_card)
        player_a_lotto.check_prizes(player_name="Player A (3 Matches)")
        
        # Player C with 6 matches (Jackpot)
        player_c_card = [12, 36, 18, 59, 26, 54]
        player_c_lotto = LotteryGame(winning_numbers, player_c_card)
        player_c_lotto.check_prizes(player_name="Player C (6 Matches - Jackpot)")
    
    def run_demo(self):
        """Function to demonstrate the full functionality of the OOP classes."""
        print("===============================================")
        print("      IT5L Examination - OOP Demonstration 🚀  ")
        print("===============================================")
        
        # Run all demos
        self.run_flames_demo()
        self.run_grading_system_demo()
        self.run_lottery_game_demo()

        print("\n===============================================")
        print("            Program Execution Complete!         ")
        print("===============================================")


# =========================================================
# Main Block to Start Execution
# =========================================================
if __name__ == "__main__":
    demo = OOPDemo()
    demo.run_demo()