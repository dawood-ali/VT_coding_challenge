Name:
- Mohamed Ali

Included Files:
	* All Those in output Directory.
	* util.py
    * vividtheory_etl.py
	* README.md

Accessories:
    * None

Running Instructions:

    1- Navigate to the directory where all the Included files reside in.
    2- Run the command 'pip install -r requirements.txt' to install the required dependencies needed to run the solution.
    3- Navigate to vividtheory_etl.py and change the variable ' PATH_TO_DATASET ' if it's different from the value already set.
    3- Run the command 'python ./vividtheory_etl.py'

Notes and Assumptions:

    * It's assumed that if a vehicle entry in the provided dataset is missing the field value of 'Year' then it violates both the hasYear and validYear validation rule.
    * A sample output has been generated by running the code and the output is stored in the ./output directory.
    * It's assumed that the output of the program needs to be displayed to the terminal only and not saved to an independent file.
    * It's assumed that the user has Python 3.9 or above installed on their system and that the path to python.exe is added to their PATH environment variable.

