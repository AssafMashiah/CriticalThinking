'''
Created on 2014-01-02

@author: Gord
'''

from dancer import Dancer
import dancer_set

class dancer_parser(object):

    def __init__(self, dancersFile):
        try:
            self.file = open(dancersFile, 'r')
            print("Successfully opened {0}".format(dancersFile))
        except:
            # todo: find the actual exceptions that should be caught
            print("Error: could not find file.")
            self.file = 0
        
    def parse_to_dancer_set(self):
        # name|email|lead/follow|code
        set = dancer_set.dancer_set()
        count = 0
        
        for line in self.file:
            arr = line.split("|")
            if (len(arr) != 4):
                print("Error: file contains incorrectly formatted line.")
                print(line)
            else:
                name = arr[0]
                email = arr[1]
                isLead = arr[2].lower() == "lead"
                code = arr[3]

                d = Dancer(name, email, isLead, code)
                print(d.toStringNumName())
                set.addDancer(d)
                count += 1
                print(d.toStringNumName())
        
        print("Finished parsing {0} lines.".format(str(count)))
        self.file.close()        
        return set
        