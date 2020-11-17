'''
Created on 2013-01-08

@author: Gord
'''

import emailer
import random
import re

class dancer_set(object):
    '''
    A set of dancers, split into partners and leads
    For use in a partner search
    '''
   
    def __init__(self):
        self.leads = list()
        self.follows = list()
        self.matchesMade = 0
        self.iterationCursor = 0
        self.dancersDict = dict()
        self.nonAlphaNumeric = re.compile('[\W_]+')
    
    def addDancer(self, dancer):
        ## Adds a dancer to the appropriate list
        
        dancer.code = self.nonAlphaNumeric.sub('', dancer.code)
        if(dancer.isLead):
            self.leads.append(dancer)
        else:
            self.follows.append(dancer)
        print('append dancer with code: ' + dancer.code)
        self.dancersDict[dancer.code] = dancer
        print('keys: ' + str(self.dancersDict.keys()))
            
    def removeDancer(self, code):
        for i in range(len(self.leads)):
            if self.leads[i].code == code:
                self.leads.pop(i)
                break
        
        for j in range(len(self.follows)):
            if self.follows[j].code == code:
                self.follows.pop(j)
                break
                
    def getDancerByCode(self, code):
        print('getting dancer with code ' + code)
        dancer = self.dancersDict[code]
        return dancer

                
    def setChoicesByCode(self, code, choices):
        choices = [self.nonAlphaNumeric.sub('', choice) for choice in choices]
        choices = [choice for choice in choices if len(choice) == 1]
        try:
            one = self.getDancerByCode(str(code))
        except KeyError as e:
            print(e.args)
        else:
            print(str(one) + ' likes: ')
            if one != None:
                sel = []
                for c in choices:
                    c = self.nonAlphaNumeric.sub('', c)
                    sel.append(c)
    #                 if len(c) > 0:
    #                     two = self.getDancerByCode(c)
    #                     if two != None:
    #                         sel.append(two)
    #                         print(c)
                one.set_choices(sel)
            print(one.code + ' : ' + str(one.choices))
    
    def sendEmails(self, mailer):
        ## Sends match emails to everyone in the set
        if(self.matchesMade == 1):
            for i in range(len(self.leads)):
                mailer.sendEmail(self.leads[i])
            for j in range(len(self.leads)):
                mailer.sendEmail(self.follows[j])
            
    
    def make_matches(self):
        ## Generates matches for everyone in the set
        for i in range(len(self.leads)):
            for j in range(len(self.follows)):
                self.leads[i].match(self.follows[j])
                self.follows[j].match(self.leads[i])
        self.matchesMade = 1
    
    
    def print_matches(self):
        ## Prints everyone's matches out in the console
        if self.matchesMade == 1:
            for i in range(len(self.leads)):
                output = self.leads[i].to_string()
                output += ": "
                output += "\n"
                output += self.leads[i].get_matches_string()
                print(output)
            
            print() ## newline
            
            for j in range(len(self.follows)):
                output = self.follows[j].to_string()
                output += ": "
                output += self.follows[j].get_matches_string()
                print(output)
        else:
            print("Matches not made\n")
    
    def printLeads(self):
        for i in range(len(self.leads)):
            print(self.leads[i].to_string())
            
    def printFollows(self):
        for i in range(len(self.follows)):
            print(self.follows[i].to_string())
    
    def resetBusy(self):
        for i in range(len(self.leads)):
            self.leads[i].busy = 0
        for j in range(len(self.follows)):
            self.follows[j].busy = 0
            
    def makeDancePairings(self):
        ## Not tested
#         random.shuffle(self.leads)
#         random.shuffle(self.follows)
        
        ## alg idea. Create all matchings first with progressive offset
        ## then shuffle the order
        
        print(str(len(self.leads)) + ", " + str(len(self.follows)))
        
        bigGroup = self.leads if len(self.leads) > len(self.follows) else self.follows
        smallGroup = self.follows if bigGroup == self.leads else self.leads 
        allPairings = list()

        for offset in range(0,min(len(self.leads), len(self.follows))):      
            pairing = list()
            print('outer loop')
            self.resetBusy()
            
            random.shuffle(bigGroup)
            random.shuffle(smallGroup)
            
            for i in range(len(smallGroup)):
                i = (i + offset) % len(smallGroup)
                print('inner loop, i = ' + str(i))
                
                if smallGroup[i].busy == 0:
                    
                    for j in range(len(bigGroup)):
                        if bigGroup[j].busy == 0 and smallGroup[i].busy == 0:
                        
                            if not smallGroup[i].hasDancedWith(bigGroup[j]):
                                match = smallGroup[i].toStringNumName() + " and " \
                                        + bigGroup[j].toStringNumName()
                                bigGroup[j].busy = 1
                                smallGroup[i].busy = 1  
                                pairing.append(match)
                                smallGroup[i].danceWith(bigGroup[j])
                                bigGroup[j].danceWith(smallGroup[i])
                                break       
                                
            
            for d in bigGroup:
                if d.busy == 0:
                    match = d.toStringNumName() + " alone "
                    pairing.append(match)        
                        
            allPairings.append(pairing)
        
        self.resetBusy()    
        random.shuffle(allPairings)
        return allPairings
        
    def undoLastDanceMatches(self):
        for i in range(len(self.leads)):
            if len(self.leads[i].dancedWith) != 0:
                self.leads[i].dancedWith.pop()
        
        for j in range(len(self.follows)):
            if len(self.follows[j].dancedWith) != 0:
                self.follows[j].dancedWith.pop()
            
    def setup(self):
        ## previously added dancers here
        print("Did nothing.")