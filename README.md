# spoj-tools

Requirement: Python 3.2 or higher

main.py contains the main menu which runs all the other scripts. Please change the line 2 of main.py before use.

# spoj-friends.py

This python script takes one username and a list of one or more of his friends. The script then lists all the problems solved by his friend(s) and not by himself in sorted order of number of users who have solved that question. It can thus suggest the next problem that a user can solve.

usage: python spoj-friends.py

# spoj-viewer.py

This script loads the problem statement given a question code as input.

usage: python spoj-viewer.py &lt;problemcode&gt;

# spoj-submitter.py

This python script is a Command Line Solution Submitter for spoj.com.Your login credentials are stored in a pickle file. If the file is found next time then it logs in automatically otherwise you need to login again. To login from other user's account you have to delete the pickle file.Once you are logged in you are asked to select from the languages available for that question. The script returns the verdict of the solution - along with the time and the memory consumed.

usage: python spoj-submitter.py &lt;filename&gt; &lt;problemname&gt;

#.vimrc

The following .vimrc config file code enables the scripts to be run from within vim. So you can view a problem, code and submit directly from the vim terminal. 
The usage is as follows:

1. To view a problem - :VW &lt;problem-code&gt;
2. To submit a problem - :SB &lt;problem-code&gt;

Please change line 1 to the path where you have installed spoj-tools.
