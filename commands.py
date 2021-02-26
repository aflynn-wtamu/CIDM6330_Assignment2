'''
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
'''
from datetime import datetime
import sys

from database import DatabaseManager

# module scope
db = DatabaseManager('bookmarks.db')

class CreateBookmarksTableCommand:
    '''
    uses the DatabaseManager to create the bookmarks table
    '''
    def execute(self):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'date_added': 'text not null',
        })


class AddBookmarkCommand:
    '''
    This class will:

    1. Expect a dictionary containing the title, URL, and (optional) notes information for a bookmark.
    2. Add the current datetime to the dictionary as date_added. 
    3. Insert the data into the bookmarks table using the DatabaseManager.add method.
    4. Return a success message that will eventually be displayed by the presentation layer.
    '''
    def execute(self, data):
        data['date_added'] = datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return 'Bookmark added!'


class ListBookmarksCommand:
    '''
    We need to review the bookmarks in the database.
    To do so, this class will:
    1. Accept the column to order by, and save it as an instance attribute. 
    2. Pass this information along to db.select in its execute method.
    3. Return the result (using the cursor’s .fetchall() method) because select is a query.
    '''
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()


class DeleteBookmarkCommand:
    '''
    We also need to remove bookmarks.
    '''
    def execute(self, data):
        db.delete('bookmarks', {'id': data})
        return 'Bookmark deleted!'


class QuitCommand:
    def execute(self):
        sys.exit()



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