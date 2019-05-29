import urwid
import TodoGuiFunctions

choices = ['Add Task','Delete Task','Edit Task','Mark Task As Completed','Pending Tasks','Completed Tasks','All Tasks','Exit']


def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        urwid.connect_signal(button, 'click', item_chosen, c)
    return urwid.ListBox(urwid.SimpleFocusListWalker(body)) 


def item_chosen(button, choice):
    done = urwid.Button(u'Ok')
    if choice == 'Add Task':
        response = urwid.Text([u'You chose ', choice, u'\n'])
        urwid.connect_signal(done, 'click', TodoGuiFunctions.AddTask)
        main.original_widget = urwid.Filler(urwid.Pile([response,
            urwid.AttrMap(done, None, focus_map='reversed')]))
    elif choice == 'Delete Task':
        response = urwid.Text([u'You chose ', choice, u'\n'])
        urwid.connect_signal(done, 'click', exit_program)
        main.original_widget = urwid.Filler(urwid.Pile([response,
            urwid.AttrMap(done, None, focus_map='reversed')]))
    elif choice == 'Exit':
        urwid.ExitMainLoop()


def exit_program(button):
    raise urwid.ExitMainLoop()


main = urwid.Padding(menu(u'To Do App', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)


def running(title):
    while True:
        urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()


if __name__ == '__main__':
    running('Running')