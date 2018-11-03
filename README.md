# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

#Instructions for execution & tests:
1. In your terminal, goto the folder structure where you see input folder, output folder, src folder, insight_testsuite folder and run.sh.
2. run.sh will execute the h1b_counting.py file inside the src folder. 
3. To execute the run.sh script, type: ./run.sh in your terminal. 
4. To test whether the script passes the insight test, goto insight test suite and type: ./run_tests.sh 

# Solution:

This python program basically takes the old H1B datasets (2014, 2015, 2016) that are available in CSV file formats and processes them to find the following information: 
1. TOP OCCUPATIONS THAT RECEIVED A H1B CERTIFICATION
2. TOP STATES WHERE THE H1B WORKERS ACTIVELY WORK (WORK SITE)


# IDENTIFYING THE COLOUMN OF INTEREST IN THE DATASET: 

All the inputs are CSV files of the year 2014, 2015, 2016 and are placed in the INPUT folder structure. The input files have the columns such as 'STATUS' or 'LCA_CASE_STATUS' which describe the candidate's H1B application status. The column 'LCA_CASE_SOC_NAME' or 'SOC_NAME' describes the name of the applicant's occupation. The column "WORKSITE_STATE" or LCA_CASE_WORKLOC1_STATE describes where the candidate location of work is. The dataset has different column heading in different years. Thus the first step is to handle this change in names and identify the column of interest. 

# CHOICE OF DATASTRUCTURE: 

The CSV file is basically an accumulation of candidates and each candidate has some X number of features which take a particular value. This can be thought as a LIST OF DICTIONARIES. Each row (candidate) is a dictionary. The first row of the CSV file describes the heading and this will be seen as the Key of our dictionary. The number of the rows (candidates) in the CSV file define the length of the list. CSV file thus becomes a list of same type of dictionary whose keys are defined in the first row of the CSV file. 

# makedicts function: 

This function takes the CSV file as the input, traverses throughout the CSV and makes a list of dictionary. This is realised by the function called DictReader. Once the CSV file is imported as a dictionary, then I check whether a candidate's "STATUS" is "CERTIFIED"; if yes then the program makes two new dictionaries. One to maintain the occupation of the candidate and its count. The second dictionary for maintaining the worksite location and its count. This operation is performed throughout the CSV file. 

Once the two dictionaries are created, they are sorted in the descending order of their counts. This is then followed by sorting of ascending order of Keys. Since the value in both of the dictionaries are numbers, we take an advantage of that and just sort the [-values] in ascending order. This achieves the required objective. 

#Writefiles function: 

This function writes our dictionaries into TOP_10_OCCUPATIONS.txt and TOP_10_STATES.txt. 

#INPUT FILES: 

Input files are stored on the input folder

#OUTPUT FILES: 

Output files are stored in the output folder. 

#SOURCE FILES: 

h1b.py contains all the functions necessary to process the data and write the data in the appropriate folder. 
h1b_counting.py is the main file which executes the functions necessary on the input folder. 

#TESTS: 
These source files were tested with 2014, 2015, 2016 year H1B data and successfully passed. The Insight_test_suite was also run and the src files passed the test. 

## Repo directory structure

The directory structure for your repo:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_counting.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── temp-test_1
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```

