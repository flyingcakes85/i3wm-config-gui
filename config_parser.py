import os.path

homedir = os.path.expanduser("~")


class Config:
    bindsym_dict = {}
    set_dict = {}
    exec_list = []
    exec_always_list = []


def get_i3_config():
    i3_config_file = open(homedir + "/.config/i3/config", "r")
    config = Config()

    for line in i3_config_file:
        line = line.strip()
        phrases = line.split(sep=" ")

        if phrases[0].strip() == "bindsym":
            config.bindsym_dict[phrases[1]] = " ".join(phrases[2:])
        elif phrases[0].strip() == "set":
            config.set_dict[phrases[1]] = " ".join(phrases[2])
        elif phrases[0].strip() == "exec":
            if phrases[1] == "--no-startup-id":
                config.exec_list.append((" ".join(phrases[2:]), True))
            else:
                config.exec_list.append((" ".join(phrases[1:]), False))
        elif phrases[0] == "exec_always":
            if phrases[1] == "--no-startup-id":
                config.exec_always_list.append((" ".join(phrases[2:]), True))
            else:
                config.exec_always_list.append((" ".join(phrases[1:]), False))

    i3_config_file.close()
    return config
