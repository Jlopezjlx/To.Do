import FunctionsGui
import todogui
from time import sleep 
import urwid


def exit_program(button):
    raise urwid.ExitMainLoop()


def AddTask(title):
    Save = urwid.Button('Save')
    Done = urwid.Button('Ok')
    Exit = urwid.Button('Exit')
    Text = urwid.Text('Add Task\n')
    TitleText = urwid.Text('Type a Task Title: ')
    TitleInput = urwid.Edit(multiline=True)
    StartDateText = urwid.Text('Type an Start Date Ex. 03/04/2019(D,M,Y): ')
    StartDateInput = urwid.Edit(multiline=True)
    DueDateText = urwid.Text('Type an Due Date Ex. 03/04/2019(D,M,Y): ')
    DueDateInput = urwid.Edit(multiline=True)
    DescriptionText = urwid.Text('Type a Description Max. 100 words:  ')
    DescriptionInput = urwid.Edit(multiline=True)
    priorityText = urwid.Text('Choose a Priority, Options:\n1.High\n2.Medium\n3.Low\nSelected Option: ')
    PriorityInput = urwid.Edit(multiline=True)
    urwid.connect_signal(Exit, 'click', exit_program)
    urwid.connect_signal(Save, 'click', FunctionsGui.savetask, [TitleInput,StartDateInput,DueDateInput,DescriptionInput,PriorityInput])
    urwid.connect_signal(Done, 'click', todogui.running)
    main = urwid.Padding(urwid.Filler(urwid.Pile([Text,TitleText,TitleInput,StartDateText,StartDateInput,DueDateText,DueDateInput, DescriptionText,DescriptionInput,priorityText,PriorityInput,
        urwid.AttrMap(Save, None, focus_map='reversed'),urwid.AttrMap(Done, None, focus_map='reversed'),urwid.AttrMap(Exit, None, focus_map='reversed')])), left=2, right=2)
    top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
        align='center', width=('relative', 80),
        valign='middle', height=('relative', 80),
        min_width=20, min_height=9)
    urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

if __name__ == '__main__':
    pass