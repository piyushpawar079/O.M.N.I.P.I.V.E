from OMNIPIVE.Functions.basic_functions import Basic_functions
from OMNIPIVE.GUI.main_gui import imageHandler


class Check:

    bf = Basic_functions()
    ih = imageHandler()

    def in_Basic_functions(self, query):
        mappings = {
            'introduction': self.bf.introduce,
            'ip address': self.bf.ip_address,
            'joke': self.bf.tell_jokes,
            'alarm': self.bf.set_alarm,
            'take screenshot': self.bf.take_screenshot,
            'wait': self.bf.wait,
            'battery': self.bf.battery,
            'functions': self.bf.function,
            'exit': self.bf.exit,
            'take notes': self.bf.take_notes,
            'minimize': self.ih.minimize_gui
        }

        for i in mappings.keys():
            if i in query.lower() or query.lower() in i:
                mappings[i]()
                return True



