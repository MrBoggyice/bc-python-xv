"""
	basically what i am about to do is create
	an app used for taking notes using oop
	and this version NotesApplication is currently
	running on the terminal, there are no UIs or DBs
	the notes are simply stored on a list.
	And this note taking application has all the basic
	functionality of an actual note taking application
	with pretty UIs and databases.

	~fortune iyke
	~enjoy
"""

class NotesApplication (object): 
	def __init__(self,author=None): # the initialisation of the NoteApplication object for which the author parameter is  first initialized to None
		self.author = author
		self.note_name = [] # This is an empty list which holds the created note in a list 

	def create(self,note_content): # The create method basically allows notes to be created within the note_content parameter
		self.note_content = note_content
		self.note_name.append(self.note_content) #The created note is now appended into that empty list

	def list(self): # Here this list method allows the created notes to be listed based on the index number of that list
		self.ls = ''
		for i in self.note_name: # loops througn the list of the created notes
			self.i_idex = self.note_name.index(i) # and returns the index number of the particular note
			self.ls = "Note ID: %s \n %r \n By Author: %s" % (self.i_idex, self.note_name, self.author) # the variable self.ls holds the note in our required format
			print self.ls # and then self.ls is printed

	def get(self,note_id): # this get method takes in the index number of a particular note and returns the note in a string 
		self.note_id = note_id
		print str(self.note_name[int(self.note_id)]) # prints in a string format
		

	def search(self, search_text): # the search method takes in a string to lookup in the notes created in the list
	    if search_text != "": # this line checks if an empty string was passed in
	    	add = "Showing results for search \"[<"+search_text+">]\"" # the add variable holds the required format it should be returnd and the value of the search_text
	    	for i in self.note_name: # loops the list of the created notes and \
	    		if search_text in i: # if the search_text is in i it \
	    			note_id = self.note_name.index(i) # holds the index of the created note in the list in note_id variable and  \
	    			add += "\n Note ID: %d \n %s \n By Author %s"%(note_id, i, self.author) # adds the format with the rest of the required data
	    		else: 
	    			print 'sorry! its not found' #if the string wasn't found in any of the created lists
	      	print str(add) #it prints the result in string format

	def delete(self,note_id):# the delete method simply deletes a created note from the list using its note_id aka index number
		self.note_name.pop(int(note_id))

	def edit (self,note_id,new_content): #while edit simply overwrites an exisiting note using it's note_id
		self.note_name[int(note_id)]=new_content
'''
	the code below allows the NotesApplication
	to be used on a command line terminal
	as we make the first instance of an object
	using the raw_input to request it from the user
'''

author = raw_input('Enter the name of the Author: ') # takes the user's name as the author and stores it in variable author
fortune = NotesApplication(author) # fortune the actual note application takes the author's name
def action():# this function basically allows easy communication of the note application with its user on the command line
	what_to_do = raw_input("Press 1 to create a note \n Press 2 list the available notes \n Press 3 to get a particular list \n Press 4 to search for a note \n press 5 to delete a note \n Press 6 to edit a note:")
	if what_to_do == '1':
		notecreated = raw_input("Please create a note: ")
		fortune.create(notecreated)
		print "Your note has been created"
		action()

	if what_to_do == '2':
		print "Here is your note:"
		fortune.list()
		action()

	if what_to_do == '3':
		get_with_note_id = raw_input('what is your note id: ')
		int(get_with_note_id)
		fortune.get(get_with_note_id)
		action()
		
	if what_to_do == '4':
		what_to_search = raw_input('what are you looking for: ')
		fortune.search(what_to_search)
		action()

	if what_to_do == '5':
		what_to_delete = raw_input('what is the note ID of what you wish to delete: ')
		int(what_to_delete)
		fortune.delete(what_to_delete)
		action()

	if what_to_do == '6':
		note_id_to_edit = raw_input('what is the Note ID: ')
		new_stuff_added = raw_input('what changes would you like to make on that note: ')
		fortune.edit(note_id_to_edit, new_stuff_added)
		action()



action() 