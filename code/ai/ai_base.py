
'''
Language : Python 3.x
email : andrew@openmarmot.com
notes : define some common functions for the class
'''


#import built in modules

#import custom packages

class AIBase(object):
    def __init__(self):
        self.loaded=False
        self.llm=None
        pass

    def generate_response(self,question):
        pass
          
    def load(self):
        pass
    
    def unload(self):
        pass


