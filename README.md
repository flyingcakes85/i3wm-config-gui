# i3wm config gui

## Test on Arch Linux (or Arch based distro)

1. Install dependencies

 ```sh
 sudo pacman -S python cairo pkgconf gobject-introspection gtk3
 ```

2. Clone this repo
  ```sh
  git clone https://github.com/flyingcakes85/i3wm-config-gui
  cd i3wm-config-gui
  ```

3. Create virtual environment
  ```sh
  python -m venv test
  source test/bin/activate
  ```

4. Get packages
  ```sh
  pip3 install pycairo
  pip3 install PyGObject
  ```

5. Run this!
  ```sh
  python config_manager_gtk.py
  ```

### Extra links

- Python GObject Getting Started : https://pygobject.readthedocs.io/en/latest/getting_started.html
- Python Gtk+ 3 Tutorial : https://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html
