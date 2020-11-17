Partner-Search
==============
A set of scripts for use in a partner search. Created for use by UBC Dance Club.

Dancers File (for option 0) should be formatted as follows, line by line:
<name>|<email>|<lead or follow>|<code>

Choices File (for option 1) should be formatted as follows, line by line:
<code>|<code of choice>,<code of choice>,<code of choice>,...

If in doubt, compare to the files dancersTest.txt and choicesTest.txt

Dance matchings (option 2) produces a timestamped file with all dances on it. People not dancing are included so you can pair them with latecomers. There is a possibility of problems if an equal number of leads and follows show up. Open the file with a text editor (notepad, textedit).

Partner matching (option 3) prints out matches to the console. It also has the option to email everyone with their matches. The email function hasn't been tested (it worked last year though), FYI.
