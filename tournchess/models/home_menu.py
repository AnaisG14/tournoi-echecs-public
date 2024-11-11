class HomeMenu:
    """ Model for the home menu """

    def __init__(self):
        self.menu_entries = {}
        self.auto_key = 1

    def add_item(self, key, entries, controller=""):
        """ Add item to the menu"""
        if key == "auto":
            key = str(self.auto_key)
            self.auto_key += 1
        self.menu_entries[key] = (entries, controller)
        return

    def __repr__(self):
        return f"{self.menu_entries}"
