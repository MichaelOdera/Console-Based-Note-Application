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
    
  
    def next_id(self):
        try:
            return max(self.notes_dict.keys())+1
        except ValueError:
            return 1
    

    def createNote(self, note_content):
        self.notes_dict[self.next_id()] = note_content 
        print self.notes_dict
    

    def viewNote(self, note_id):
        try:
            self.search_input = int(note_id) 
            print (self.notes_dict.get(self.search_input, "The note ID could not be found  \n"))
        except ValueError:
            print ("You did not enter an integer. Please re-enter a digit: \n")
     

    def deleteNote(self, note_id):
        try:
            self.del_Noteval = int(note_id) 
            if self.del_Noteval in self.notes_dict.keys():
                del self.notes_dict[self.del_Noteval]
                print ("Here is your formatted list \n")
                print (self.notes_dict)
        except ValueError:
            print("All note IDs are in digit number form please enter a digit: \n")

    def notelist(self, end_lim_par):
        end  = int(end_lim_par)
        if end <= len(self.notes_dict):
            print(self.notes_dict.values()[0:end])
        else:
            print("This is an invalid limiting parameter")

    def search_word(self, query_string):
        self.sample_search = query_string 
        foundsearch_notelist = []
  
        for k, v in self.notes_dict.items():
            if self.sample_search in v:
                print(k, v)
                
        foundsearch_notelist.append(v)


    def next_Note(self, next_word):
        count = 0
        self.sorted_list = []

        self.sorted_list.extend(foundsearch_notelist[1:20])
        while count < len(self.sorted_list):
            next_noteView = next_word
            if next_noteView == "next":
                print(self.sorted_list[count])
                count += 2

    def import_json(self, note_id):
        try:
            self.datato_load = int(note_id)
            if self.datato_load in self.notes_dict.keys():
                imported_data = json.load(self.datato_load)
                imported_data_list.append(imported_data)
                print(imported_data_list)
            else:
              print("There no such file")
        except ValueError:
            print("There was no such data found to be exported.")

    def export_json(self, jsonfile_id):
        self.datato_dump = jsonfile_id
        try:
            if self.datato_dump in self.imported_data_list:
                exported_data = json.dump(self.datato_dump)
                print(exported_data)
        except ValueError:
            print("No such item found in the json list")
