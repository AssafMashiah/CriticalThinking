import datetime
import sys
import dancer_set
import emailer
from dancer_parser import dancer_parser
from match_parser import match_parser


def print_main_options():
    print("""What would you like to do?
    
    0: Set the dancers participating
    1: Set the choices of dancers
    2: Create pairings for each round of dancing 
    3: Perform the matching
    """)


def setup_dancers():
    file_ = raw_input("Enter the name of the file containing the dancer info: ")
    parser = dancer_parser(file_)
    the_set = parser.parse_to_dancer_set()
    num_dancers = len(the_set.leads) + len(the_set.follows)
    print("Setup " + str(num_dancers) + " dancers.")
    return the_set


def setup_choices(dance_club):
    user_input = raw_input("Enter the name of the file containing the dancer's choices: ")
    parser = match_parser(user_input)
    parser.parse_choices_to_set(dance_club)


def do_pairings(dance_club):
    all_pairings = dance_club.makeDancePairings()
    time_stamp = str(datetime.datetime.now())
    file_name = "pairings-" + time_stamp + ".txt"
    file = open(file_name, 'w')
    count = 0
    print("Made " + str(len(all_pairings)) + " pairings")

    for pairing in all_pairings:
        count += 1
        file.write("Matching " + str(count) + " of " + str(len(all_pairings)) + "\n")
        for match in pairing:
            line = match.replace('\n', '').replace('\r', '')
            file.write(line + '\n')

    file.close()


def do_matching(dance_club):
    ## Make the matches and print them in the console
    dance_club.make_matches()
    dance_club.print_matches()

    user_input = raw_input("Would you like to send emails at this time? (yes/no): ")
    if user_input.lower() == "yes":
        user_input = raw_input("Are you sure? (yeah, nope): ")

        if user_input.lower() == "yeah":
            # Setup the emailer and send out the emails
            mailer = emailer.emailer()
            dance_club.send_emails(mailer)
            mailer.quitEmail()
            print("Done!")


def main():
    print("""Welcome to Partner Search
    
    This program allows you to run a ballroom dance partner search (or speed-dating, as they are the same thing)
    """)

    dance_club = dancer_set.dancer_set()

    while True:
        while True:
            try:
                print_main_options()
                user_input = int(raw_input("Select function (0,1,2,3): "))
                valid_options = [0, 1, 2, 3]

                if user_input in valid_options:
                    print("")
                    break
                else:
                    print("Error: invalid function selection.")

            except ValueError:
                print("Error: you must enter a valid integer.")

        if user_input == 0:
            dance_club = setup_dancers()
        elif user_input == 1:
            setup_choices(dance_club)
        elif user_input == 2:
            do_pairings(dance_club)
        elif user_input == 3:
            do_matching(dance_club)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nUser keyboard interrupt")
