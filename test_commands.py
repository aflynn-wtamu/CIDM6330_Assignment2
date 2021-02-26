# Commands Test
import unittest
import commands

class CommandTestCase(unittest.TestCase):
    
    def test_AddBookmarkCommand(self):
        # arrange
        expected_result = 'Bookmark added!'
        expected_count = len(commands.ListBookmarksCommand().execute())+1

        # act
        entry = {'title': 'test',
                'url': 'www.test.com',
                'notes': 'test notes'}
        actual_result = commands.AddBookmarkCommand().execute(entry)
        actual_count = len(commands.ListBookmarksCommand().execute())

        #assert
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_count, actual_count)
    
    
    def test_ListBookmarksCommand(self):
        # arrange
        #print(commands.ListBookmarksCommand().execute())
        expected_result = [(1, 'w3schools', 'https://www.w3schools.com/', 'Great reference', '2021-02-20T21:14:25.502283'),
                        (2, 'test', 'www.test.com', 'test notes', '2021-02-21T16:35:31.008368')]
        
        # act
        actual_result = commands.ListBookmarksCommand().execute()

        # asset
        self.assertEqual(expected_result, actual_result)
    

    def test_ListBookmarksCommand_orderTitle(self):
        # arrange
        #print(commands.ListBookmarksCommand().execute())
        expected_result = [(2, 'test', 'www.test.com', 'test notes', '2021-02-21T16:35:31.008368'),
                        (1, 'w3schools', 'https://www.w3schools.com/', 'Great reference', '2021-02-20T21:14:25.502283')]
        
        # act
        actual_result = commands.ListBookmarksCommand(order_by='title').execute()

        # asset
        self.assertEqual(expected_result, actual_result)


    def test_DeleteBookmarkCommand(self):
        # arrange
        bookmark_dict = commands.ListBookmarksCommand().execute()
        expected_result = 'Bookmark deleted!'
        expected_count = len(bookmark_dict)-1
        remove_record_id = bookmark_dict[expected_count][0]

        #act
        actual_result = commands.DeleteBookmarkCommand().execute(remove_record_id)
        actual_count = len(commands.ListBookmarksCommand().execute())

        #assert
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_count, actual_count)