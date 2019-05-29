import tododb 
import todogui
import urwid

#calling mongo confings 
mongo = tododb.mongo_configs()        


#define function to save task in mongo
def savetask(title,data):
    try:
        title,startdate,duedate,description,priority = data
        task = {
            "title" : title.edit_text, 
            "dates": [{
                "startdate": startdate.edit_text,
                "duedate":duedate.edit_text
            }],
            "description": description.edit_text,
            "priority": priority.edit_text,
            "state": "Pending",
            "porcentage": 0
        }
        mongo.insert_one(task)
        Exit = urwid.Button('Ok')
        Text = urwid.Text('Task has been added\n')
        urwid.connect_signal(Exit, 'click', todogui.running)   
        main = urwid.Padding(urwid.Filler(urwid.Pile([Text,
            urwid.AttrMap(Exit, None, focus_map='reversed')])), left=2, right=2)
        top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=20, min_height=9)
        urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
    except:
        Exit = urwid.Button('Ok')
        Text = urwid.Text('Error Adding Data\n')
        urwid.connect_signal(Exit, 'click', todogui.running)   
        main = urwid.Padding(urwid.Filler(urwid.Pile([Text,
            urwid.AttrMap(Exit, None, focus_map='reversed')])), left=2, right=2)
        top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=20, min_height=9)
        urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
