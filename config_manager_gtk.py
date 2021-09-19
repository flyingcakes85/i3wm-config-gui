from config_parser import Config, get_i3_config
import gi

gi.require_version("Gtk", "3.0")  # noqa
from gi.repository import Gtk  # noqa


class ConfigWindowGtk(Gtk.Window):

    def __init__(self, config):
        super().__init__(title="i3wm Config Manager")

        notebook = Gtk.Notebook()
        self.add(notebook)

        bindsym_page = Gtk.ScrolledWindow()
        bindsym_page.set_border_width(10)

        exec_page = Gtk.Box()
        exec_page.set_border_width(10)
        exec_page.add(Gtk.Label(label="Autostart Page"))

        colors_page = Gtk.Box()
        colors_page.set_border_width(10)
        colors_page.add(Gtk.Label(label="Colors Page"))

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        bindsym_page.add(listbox)

        for key, value in config.bindsym_dict.items():
            box_temp = Gtk.Box(
                orientation=Gtk.Orientation.HORIZONTAL)

            textview = Gtk.TextView()
            textbuffer = textview.get_buffer()
            textbuffer.set_text(f"{key} - {value}")
            box_temp.pack_start(textview, True, True, 0)
            row_temp = Gtk.ListBoxRow()
            row_temp.add(box_temp)
            listbox.add(row_temp)

        notebook.append_page(
            bindsym_page, Gtk.Label(label="Keybindings"))
        notebook.append_page(
            colors_page, Gtk.Label(label="Colors"))
        notebook.append_page(
            exec_page, Gtk.Label(label="Autostart"))


def main():
    config = get_i3_config()
    config_win = ConfigWindowGtk(config)
    config_win.resize(500, 500)
    config_win.connect("destroy", Gtk.main_quit)
    config_win.show_all()
    Gtk.main()

    # print(config.bindsym_dict)


if __name__ == "__main__":
    main()
