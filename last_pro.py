import sqlite3 as lighted
import json

class noteTaking(object):
    print("///////////////////////////////////////")
    print("//  WELCOME TO THIS NOTE TAKING APP ///")
    print("///////////////////////////////////////")
    print("\n")
    print("\n")


    notes_dict = {}
    search_input = ""
    del_Noteval = ""
    notes_input = ""
    sample_search = ""


    def __init__(self):
        self.notes_input = ""
    
    # This is an autogenerating key method for dictionaries to be created.
    def next_id(self):
        try:
            return max(self.notes_dict.keys())+1
        except ValueError:
            return 1
    
    # This is the function that allows the user to create a note
    def createNote(self, note_content):
        self.notes_dict[self.next_id()] = note_content 
        print self.notes_dict
    
    # This is a function that allows the user to view a single note .
    def viewNote(self, note_id):
        try:
            self.search_input = int(note_id) 
            print (self.notes_dict.get(self.search_input, "The note ID could not be found  \n"))
        except ValueError:
            print ("You did not enter an integer. Please re-enter a digit: \n")
     
    # This is the method that allows the user to delete a single note in the dictionary created
    def deleteNote(self, note_id):
        try:
            self.del_Noteval = int(note_id) 
            if self.del_Noteval in self.notes_dict.keys():
                del self.notes_dict[self.del_Noteval]
                print ("Here is your formatted list \n")
                print (self.notes_dict)
        except ValueError:
            print("All note IDs are in digit number form please enter a digit: \n")

    # This is the function that allows the user to view the list of notes and can a set a limit to the number of notes he can view
    def notelist(self, end_lim_par):
        end  = int(end_lim_par)
        if end <= len(self.notes_dict):
            print(self.notes_dict.values()[0:end])
        else:
            print("This is an invalid limiting parameter")

    # This is a method that allows the user to create a search word that can be looked for in the list of dictionaries
    def search_word(self, query_string):
        self.sample_search = query_string 
        foundsearch_notelist = []
  
        for k, v in self.notes_dict.items():
            if self.sample_search in v:
                print(k, v)
                
        foundsearch_notelist.append(v)

    # This is a function that allows the user to view the next note every time a word is entered
    def next_Note(self, next_word):
        count = 0
        self.sorted_list = []

        self.sorted_list.extend(foundsearch_notelist[1:20])
        while count < len(self.sorted_list):
            next_noteView = next_word
            if next_noteView == "next":
                print(self.sorted_list[count])
                count += 2
    
    #This method deals with the changing of the data to json
    def import_json(self, note_id):
        try:
            self.datato_load = int(note_id)
            if self.datato_load in self.notes_dict.keys():
                imported_data = json.load(self.datato_load,'read')
                imported_data_list.append(imported_data)
                print(imported_data_list)
            else:
              print("There no such file")
        except ValueError:
            print("There was no such data found to be exported.")

    # This method allows the user to hange his data from python to json
    def export_json(self, jsonfile_id):
        self.datato_dump = jsonfile_id
        try:
            if self.datato_dump in self.imported_data_list:
                exported_data = json.dump(self.datato_dump,'write')
                print(exported_data)
        except ValueError:
            print("No such item found in the json list")
