"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    my_program note_create <note_content>... 
    my_program note_view <note_id>
    my_program note_delete <note_id>
    my_program note_search <query_string>...
    my_program next_note <next_word>
    my_program import_json <note_id>
    my_program export_json <jsonfile_id>
    my_program note_list <limit_par>
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from last_pro import noteTaking
from docopt import docopt, DocoptExit
noted = noteTaking()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '(my_program) '
    file = None

    @docopt_cmd
    def do_note_create(self, arg):
        """Usage: note_create <note_content>..."""

        noted.createNote(' '.join(arg['<note_content>']))

    @docopt_cmd
    def do_note_view(self, arg):
        """Usage: note_view <note_id>"""

        noted.viewNote(arg['<note_id>'])

    @docopt_cmd
    def do_note_delete(self, arg):
        """Usage: note_delete <note_id>"""
        
        
        noted.deleteNote(arg['<note_id>'])
    
           

    @docopt_cmd
    def do_note_search(self, arg):
        """Usage: note_search <query_string>..."""

        noted.search_word(' '.join(arg['<query_string>']))


    @docopt_cmd
    def do_next_note(self, arg):
        """Usage: next_note <next_word>"""

        noted.nextNote(arg['<next_word>'])


    @docopt_cmd
    def do_import_json(self, arg):
        """Usage: import_json <note_id>"""

        noted.import_json(arg['<note_id>'])


    @docopt_cmd
    def do_export_json(self, arg):
        """Usage: export_json <jsonfile_id>"""

        noted.export_json(arg['jsonfile_id>'])


    @docopt_cmd
    def do_notes_list(self, arg):
        """Usage: notes_list <limit_par>"""

        noted.notelist(arg['<limit_par>'])


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Please use this app again!')
        exit()


MyInteractive().cmdloop()

print(opt)