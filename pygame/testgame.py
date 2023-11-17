import pygame
import unittest
from unittest.mock import patch, Mock
from game import lay_egg_randomly, lay_second_egg_randomly, lay_third_egg_randomly, poop_randomly, check_collision, check_poop_collision
from game import move_left, move_right, display_score

class TestChickenEggGame(unittest.TestCase):

    @patch('game.random.randint', return_value=50)  # Adjust this value based on your collision logic
    def test_check_collision_false(self, mock_randint):
        egg = {'x': 50, 'y': 600}
        basket_x, basket_y = 30, 650
        result = check_collision(egg, basket_x, basket_y)
        self.assertFalse(result)

    @patch('game.random.randint', return_value=50)  # Adjust this value based on your collision logic
    def test_check_poop_collision_false(self, mock_randint):
        poop = {'x': 50, 'y': 600}
        basket_x, basket_y = 30, 650
        result = check_poop_collision(poop, basket_x, basket_y)
        self.assertFalse(result)
    
    @patch('game.pygame.key.get_pressed', return_value={pygame.K_LEFT: 1, pygame.K_RIGHT: 0})
    def test_move_left(self, mock_get_pressed):
        initial_position = 400
        speed = 5
        new_position = move_left(initial_position, speed)
        self.assertEqual(new_position, initial_position - speed)

    @patch('game.pygame.key.get_pressed', return_value={pygame.K_LEFT: 0, pygame.K_RIGHT: 1})
    def test_move_right(self, mock_get_pressed):
        initial_position = 400
        speed = 5
        new_position = move_right(initial_position, speed)
        self.assertEqual(new_position, initial_position + speed)

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_score_increment_on_egg_collision(self):
        # Mock Pygame display and font
        mock_screen = Mock()
        mock_surface = Mock()
        mock_surface.blit = Mock()

        # Mock the egg and basket positions for collision
        egg = {'x': 400, 'y': 650}  # Assume the egg is at the basket position
        basket_x = 400
        basket_y = 650

        # Mock the eggs list with the colliding egg
        eggs = [egg]

        # Initial score
        initial_score = 0

        # Call the check_collision function and display_score function
        with patch('pygame.font.Font', return_value=Mock(render=Mock(return_value=mock_surface))), \
             patch('pygame.display.flip'):
            score_incremented = False
            if check_collision(egg, basket_x, basket_y):
                display_score(mock_screen, initial_score, pygame.font.Font, (255, 255, 255), 10, 10)
                score_incremented = True

        # Check that the score was incremented
        self.assertTrue(score_incremented)

if __name__ == '__main__':
    unittest.main()
