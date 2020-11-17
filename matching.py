class Person:
    """
    Represent a generic person
    """

    def __init__(self, name, priorities):
        """
        name is a string which uniquely identifies this person

        priorities is a list of strings which specifies a ranking of all
          potential partners, from best to worst
        """
        self.name = name
        self.priorities = priorities
        self.partner = None

    def __repr__(self):
        return 'Name is ' + self.name + '\n' + \
               'Partner is currently ' + str(self.partner) + '\n' + \
               'priority list is ' + str(self.priorities)


class Boy(Person):
    """
    Represents a man
    """

    def __init__(self, name, priorities):
        """
        name is a string which uniquely identifies this person

        priorities is a list of strings which specifies a ranking of all
          potential partners, from best to worst
        """
        Person.__init__(self, name, priorities)
        self.proposalIndex = 0  # next person in our list to whom we might propose

    def next_proposal(self):
        goal = self.priorities[self.proposalIndex]
        self.proposalIndex += 1
        return goal

    def __repr__(self):
        return Person.__repr__(self) + '\n' + \
               'next proposal would be to ' + self.priorities[self.proposalIndex]


class Girl(Person):
    """
    Represents a woman
    """

    def __init__(self, name, priorities):
        """
        name is a string which uniquely identifies this person

        priorities is a list of strings which specifies a ranking of all
          potential partners, from best to worst
        """
        Person.__init__(self, name, priorities)

        # now compute a reverse lookup for efficient candidate rating
        self.ranking = {}
        for rank in range(len(priorities)):
            self.ranking[priorities[rank]] = rank

    def evaluate_proposal(self, suitor):
        """
        Evaluates a proposal, though does not enact it.

        suitor is the string identifier for the man who is proposing

        returns True if proposal should be accepted, False otherwise
        :param suitor:
        """
        return not self.partner or self.ranking[suitor] < self.ranking[self.partner]


class MatchEmAll(object):
    boys = [
        ('a', ['C', 'B', 'A', 'D']),
        ('b', ['D', 'C', 'B', 'A']),
        ('c', ['A', 'B', 'D', 'C']),
        ('d', ['A', 'B', 'C', 'D'])
    ]

    girls = [
        ('A', ['a', 'b', 'c', 'd']),
        ('B', ['b', 'c', 'd', 'a']),
        ('C', ['c', 'd', 'a', 'b']),
        ('D', ['d', 'a', 'b', 'c'])
    ]

    def __init__(self, verbose=False):
        self.verbose = verbose

    def match_boys(self):
        self._match()

    def match_girls(self):
        self._match()

    def _match(self):
        men = dict()
        for person in self.boys:
            men[person[0]] = Boy(person[0], person[1])
        un_matched_boys = men.keys()

        women = dict()
        for person in self.girls:
            women[person[0]] = Girl(person[0], person[1])

        while un_matched_boys:
            m = men[un_matched_boys[0]]  # pick arbitrary unwed man
            w = women[m.next_proposal()]  # identify highest-rank woman to which
            #    m has not yet proposed
            if self.verbose:
                print m.name, 'proposes to', w.name

            if w.evaluate_proposal(m.name):
                if self.verbose:
                    print '  ', w.name, 'accepts the proposal'

                if w.partner:
                    # previous partner is getting dumped
                    m_old = men[w.partner]
                    m_old.partner = None
                    un_matched_boys.append(m_old.name)

                un_matched_boys.remove(m.name)
                w.partner = m.name
                m.partner = w.name
            else:
                if self.verbose:
                    print '  ', w.name, 'rejects the proposal'

            if self.verbose:
                print "Tentative Pairings are as follows:"
                self.print_pairings(men)
                print

        # we should be done
        print "Final Pairings are as follows:"
        self.print_pairings(men)

    @staticmethod
    def print_pairings(person):
        for p in person.values():
            print p.name, 'is paired with', str(p.partner)


if __name__ == "__main__":
    matcher = MatchEmAll()
    matcher.match_boys()
