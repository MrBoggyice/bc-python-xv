import unittest

from note_taking_app import NotesApplication

'''

    This TDD simply tests my NotesApplication object and making sure 
    everything works as expected, starting from the initialization of 
    the object down through the edit method which is the last method.
    And guys my naming convention is quite self explainatory so I didn't 
    leave much comments explaining how each piece works.
    so have fun

    ~fortune iyke ekeruo
    ~Happy coding

'''

class NotesApplicationTestSuite(unittest.TestCase):

    def test_object_type(self):
        res = NotesApplication('fortune')
        self.assertEqual(True, type(res) is NotesApplication)

    def test_obj_instance(self):
        res = NotesApplication('fortune')
        self.assertIsInstance(res, NotesApplication)

    def test_meth_note_author(self):
        res = NotesApplication('fortune')
        self.assertEqual(res.author, 'fortune')

    def test_meth_note_name(self):
        res = NotesApplication('fortune')
        self.assertEqual(res.note_name, [])

    def test_meth_create_note(self): 
        res = NotesApplication('fortune')
        res.create('fortune is my name but you can call me iyke')
        self.assertEqual(res.note_name,['fortune is my name but you can call me iyke'])

    def test_meth_create_note_index0(self):
        res = NotesApplication('fortune')
        res.create('fortune is my name but you can call me iyke')
        self.assertEqual(res.note_name[0], 'fortune is my name but you can call me iyke')

    def test_meth_create_note_index1(self):
        res = NotesApplication('fortune')
        res.create('fortune is my name')
        res.create('you can call me iyke')
        self.assertNotEqual(res.note_name[0], 'you can call me iyke')

    def test_meth_print_list(self):
        res = NotesApplication('fortune')
        res.create('fortune is my name')
        self.assertFalse(res.list())

    def test_meth_get_note(self):
        res = NotesApplication('fortune')
        res.create('fortune is my name')
        self.assertEqual(res.get(0), 'fortune is my name')

    def test_meth_search_empty(self):
        res = NotesApplication('fortune')
        self.assertFalse(res.search(''))

    def test_meth_search_if_not_found(self):
        res = NotesApplication('fortune')
        res.create('fortune is my name')
        self.assertEqual(res.search('iyke'), None)

    def test_meth_search(self):
        res = NotesApplication('fortune')
        res.create('fortune is my name')
        self.assertEqual(res.search('fortune'), None)

    def test_meth_delete_if_nothing(self):
        res = NotesApplication('fortune')
        res.create('iyke is my name too')
        self.assertFalse(res.delete(0), [])

    def test_meth_delete(self):
        res = NotesApplication('fortune')
        res.create('Hey now brown cow')
        self.assertFalse(res.delete(0))

    def test_meth_delete_sec_note(self):
        res = NotesApplication('fortune')
        res.create('hot dogs')
        res.create('I\'ve got to eat some raw tomatoes')
        self.assertFalse(res.delete(1))


    def test_meth_edit_wrng_id(self):
        res = NotesApplication('fortune')
        res.create('hey edit me')
        self.assertFalse(res.edit(0, 'hey edit me'), 'Please enter correct Note ID.')

    def test_meth_edit_cor_id(self):
        res = NotesApplication('fortune')
        res.create('fortune talks less')
        res.edit(0, 'hey now edit me')
        self.assertEqual(res.note_name, ['hey now edit me'])

    def test_meth_edit_id_1(self):
        res = NotesApplication('fortune')
        res.create('fortune is my name')
        res.create('call me iyke too')
        res.edit(1, 'hey now brown cow')
        self.assertEqual(res.note_name[1], 'hey now brown cow')

    def test_meth_edit_id_0(self):
        res = NotesApplication('fortune')
        res.create('I\'ll make it through Andela')
        res.create('it has been written')
        res.edit(0, 'nothing go fit edit am')
        self.assertEqual(res.note_name[0], 'nothing go fit edit am')


    def test_meth_edit(self):
        res = NotesApplication('fortune')
        res.create('He\'s so good to me')
        res.create('I mean the Lord God Almighty')
        res.edit(1, 'yes and that\'s so true')
        self.assertNotEqual(res.note_name[0], 'yes and that\'s so true')



if __name__ == "__main__":
  unittest.main()