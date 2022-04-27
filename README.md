# CS491-final

The code is fully built through the automated testing, which installs the packages (pytest and coverage) and then runs the tests.

Github actions were used for integration, and then Docker is what does the continuous deployment. The tests run through pytest, with coverage printing the total report.

==========================================

Main commands:

   python3 -m coverage run -m pytest test_file.py
   
   python3 -m coverage report

Docker commands:

   docker pull andrewh427/cs491final

   docker run -it andrewh427/cs491final:latest
 
==========================================

The total coverage of the project can be seen here as well as in the automations:

battle.py - 98%

cards.py - 100%

main.py - 82%

player.py - 90%

TOTAL - 92%

==========================================

Regarding integration tests, there are at least 10 tests in test_file.py that are integration tests. Although each test is sorted by what general file it tests from, most of the tests use components from others and test the overall integration. See test_file.py for list of integration tests
