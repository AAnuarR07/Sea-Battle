import random
import os

from utils.decorators import log_action
from utils.persistence import PersistenceManager
from core.player import Player

class Game:
    def __init__(self):
        PersistenceManager.ensure_files()

        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.enemy_player = None

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def pause(self, message):
        self.clear_screen()
        print(message)
        input("\nPress Enter to continue...")

    def board_to_string(self, board):
        out = []
        out.append("    " + " ".join(str(i + 1) for i in range(board.size)))

        for i in range(board.size):
            out.append(f"{i + 1:2}  " + " ".join(board.grid[i]))

        return "\n".join(out)

    def start(self):
        while True:
            self.clear_screen()
            print("\n--- MENU ---")
            print("1 - Start Game")
            print("2 - View Logs")
            print("3 - View Statistics")
            print("4 - Clear Logs")
            print("5 - Remove Last Game")
            print("6 - Exit")

            choice = input("\nChoose option: ")

            if choice == "1":
                self.start_match()
            elif choice == "2":
                self.pause("\n--- LOGS ---\n\n" + str(PersistenceManager.load_logs()))
            elif choice == "3":
                self.show_statistics()
            elif choice == "4":
                PersistenceManager.clear_logs()
                self.pause("Logs cleared")
            elif choice == "5":
                PersistenceManager.remove_last_game()
                self.pause("Last game removed")
            elif choice == "6":
                break
            else:
                self.pause("Invalid option")

    def start_match(self):
        self.clear_screen()
        print("\n--- START ---")

        name1 = input("Player 1 name: ")
        name2 = input("Player 2 name: ")

        self.player1 = Player(name1)
        self.player2 = Player(name2)

        self.setup_player(self.player1)
        self.setup_player(self.player2)

        self.current_player = self.player1
        self.enemy_player = self.player2

        self.game_loop()

    def setup_player(self, player):
        ship_sizes = [5, 4, 3, 2, 1]

        for size in ship_sizes:
            placed = False

            while not placed:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                horizontal = random.choice([True, False])

                placed = player.board.place_ship(x, y, size, horizontal)

    @log_action
    def perform_normal_shot(self, x, y):
        result = self.enemy_player.board.receive_shot(x, y)
        return f"Shot result: {result}"

    @log_action
    def perform_nuke(self, x, y):
        if self.current_player.nuke.used:
            return "Nuke's already used"

        for i in range(x, min(x + 4, 10)):
            for j in range(y, min(y + 4, 10)):
                self.enemy_player.board.receive_shot(i, j)

        self.current_player.nuke.used = True
        return "Nuke Launched"

    @log_action
    def perform_submarine(self, col):
        if self.current_player.submarine.used:
            return "Submarine's already used"

        for i in range(10):
            self.enemy_player.board.receive_shot(i, col)

        self.current_player.submarine.used = True
        return "Submarine executed"

    def game_loop(self):
        while True:
            self.clear_screen()

            print(f"\n{self.current_player.name}'s turn")
            print("\nEnemy's board:")
            self.enemy_player.board.display_public()

            print("\nCommands:")
            print("shot")
            print("nuke")
            print("submarine")
            print("board")
            print("exit")

            command = input("\nCommand: ").strip().lower()

            if command == "board":
                self.pause(
                    "Your Board:\n\n" +
                    self.board_to_string(self.current_player.board)
                )
                continue

            if command == "exit":
                break

            result = None

            if command == "shot":
                x = int(input("X (1-10): ")) - 1
                y = int(input("Y (1-10): ")) - 1
                result = self.perform_normal_shot(x, y)

            elif command == "nuke":
                x = int(input("X (1-10): ")) - 1
                y = int(input("Y (1-10): ")) - 1
                result = self.perform_nuke(x, y)

            elif command == "submarine":
                col = int(input("Column (1-10): ")) - 1
                result = self.perform_submarine(col)

            else:
                self.pause("Unknown command")
                continue

            self.pause(result)

            if self.enemy_player.board.all_ships_sunk():
                self.pause(f"{self.current_player.name} WINS!")

                PersistenceManager.register_win(
                    self.current_player.name,
                    self.enemy_player.name,
                )

                PersistenceManager.add_log(
                    self.current_player.name,
                    self.enemy_player.name,
                    "win",
                )
                break

            self.switch_turns()

    def switch_turns(self):
        self.current_player, self.enemy_player = (
            self.enemy_player,
            self.current_player,
        )

    def show_statistics(self):
        stats = PersistenceManager.load_stats()

        text = "\n--- PLAYER STATS ---\n"

        if not stats:
            self.pause("No statistics yet")
            return

        for player, data in stats.items():
            text += f"\n{player}: {data['wins']} wins\n"
            for enemy, wins in data["against"].items():
                text += f"   vs {enemy}: {wins}\n"

        self.pause(text)