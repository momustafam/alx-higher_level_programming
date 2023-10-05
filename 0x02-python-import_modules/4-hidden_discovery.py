#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hid_mods = dir(hidden_4)
    for mod in hid_mods:
        if mod[:2] == "__":
            continue
        print(mod)
