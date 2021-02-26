# Barky Test
import unittest
import barky
import commands

from barky import Option

#arrange variables for multiple tests
expected_options = {
            'A': Option('Add a bookmark', commands.AddBookmarkCommand(), prep_call=barky.get_new_bookmark_data),
            'B': Option('List bookmarks by date', commands.ListBookmarksCommand()),
            'T': Option('List bookmarks by title', commands.ListBookmarksCommand(order_by='title')),
            'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand(), prep_call=barky.get_bookmark_id_for_deletion),
            'Q': Option('Quit', commands.QuitCommand()),
        }

expected_choices = ('a', 'b', 't', 'd', 'q')

class BarkyTestCase(unittest.TestCase):

    def test_option_choice_is_valid(self):
        # act and assert
        # loop choices
        # assert option is valid
        for choice in expected_choices:
            actual_result = barky.option_choice_is_valid(choice, expected_options)
            self.assertTrue(actual_result)
    

    def test_get_option_choice(self):
        # act and assert
        # loop choices
        # assert option results
        for choice in expected_choices:
            # guide through expected inputs
            print(f'Enter "{choice}"')
            actual_result = barky.get_option_choice(expected_options)
            self.assertEqual(expected_options[choice.upper()], actual_result)
    

    def test_get_user_input(self):
        # arrange
        expected_result = 'Test'
        
        # act
        actual_result = barky.get_user_input(f'Enter "{expected_result}"')

        # assert
        self.assertEqual(expected_result, actual_result)
    

    def test_get_new_bookmark_data(self):
        # arrange
        expected_title = '1984'
        expected_url = 'www.GO1984.com'
        expected_notes = 'An over quoted book'
        
        expected_result = {
            'title': expected_title,
            'url': expected_url,
            'notes': expected_notes,
        }

        # act
        #print(f'Enter Title: {expected_title}\nEnter URL: {expected_url}\nEnter Notes: {expected_notes}')
        actual_result = barky.get_new_bookmark_data
        print(actual_result)

        # assert
        # self.assertEqual(expected_result, actual_result)
    
    def test_get_bookmark_id_for_deletion(self):
        # arrange
        #expected_id = '9'

        # act
        #actual_result = barky.get_bookmark_id_for_deletion
        #print(actual_result)
        barky.get_bookmark_id_for_deletion
        pass