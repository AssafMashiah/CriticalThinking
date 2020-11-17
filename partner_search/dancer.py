class Dancer(object):
    """
    A class for dancers, to be used in a partner search
    """

    def __init__(self, name, email, is_lead, code):
        self.name = str(name)
        self.email = str(email)
        self.is_lead = bool(is_lead)
        self.choices = list()
        self.code = str(code)
        self.matches = list()
        self.choices = list()
        self.danced_with = list()
        print(code)
        self.busy = 0

    def set_choices(self, choices):
        self.choices = choices

    def match(self, partner):
        """
        Adds PARAM to SELFs matches if PARAM is a match
        :param partner:
        :return:
        """
        if partner.isLead != self.is_lead:
            if partner.code in self.choices and self.code in partner.choices:
                self.matches.append(partner)

    def get_first_name(self):
        names = self.name.split(" ")
        return names[0]

    def get_matches_string(self):
        """
        :return: a dancer's matches with their emails, one match/email per line
        """
        output = str()
        if len(self.matches) == 0:
            return "no matches\n\r"
        else:
            output += "\n\r"
            for i in range(len(self.matches)):
                output += "#" + str(self.matches[i].code) + " "
                output += self.matches[i].to_string()
                output += "\n\r"
            return output

    def get_match_emails(self):
        """
        Returns a list of matches' emails
        """
        output = list()
        for i in range(len(self.matches)):
            output.append(self.matches[i].email)
        return output

    def get_lead_follow(self):
        return self.is_lead

    def __str__(self):
        return self.name + " - " + self.email

    def to_string_num_name(self):
        split_name = self.name.split()
        return str(self.code) + " - " + split_name[0]

    def dance_with(self, other_dancer):
        self.danced_with.append(other_dancer.code)

    def has_danced_with(self, other_dancer):
        """
        :param other_dancer:
        :return: 1 if they have danced, 0 otherwise
        """
        if other_dancer.code in self.dancedWith:
            return 1
        else:
            return 0
