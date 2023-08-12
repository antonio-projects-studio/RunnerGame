import unittest
from main import *

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game() 
        self.player = self.game.player

    def test_npc(self):
        self.assertEqual(1, len(self.game.npc_control.npc_list))
        self.game.level = 2
        self.game.new_game()
        self.assertEqual(2, len(self.game.npc_control.npc_list))
        self.game.level = 3
        self.game.new_game()
        self.assertEqual(3, len(self.game.npc_control.npc_list))
        self.game.level = 4
        self.game.new_game()
        self.assertEqual(4, len(self.game.npc_control.npc_list))
        self.game.level = 5
        self.game.new_game()
        self.assertEqual(5, len(self.game.npc_control.npc_list))


    def test_player(self):
        self.assertEqual((self.player.x, self.player.y), PLAYER_POS)

    def test_rayCasting(self):
        self.assertEqual(self.game.npc_control.npc_list[0].player_search, False)

if __name__ == "__main__":
  unittest.main()

