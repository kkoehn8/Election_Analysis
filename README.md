# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has give us the following tasks to complete the election audit of a recent local congressional election.

1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of botes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote.

## Resources
 - Date Source: election_results.csv, PyPoll_Challenge_starter_code.py
 - Software: Python 3.7.6, Visual Studio Code 1.68.1
 
## Results
The analysis showed the following results:
- There were a total of 369,711 votes cast in the election
- The county summary for the election was:
    - Jefferson cast 10.5% of the votes for a county total of 38,855 votes.
    - Denver cast 82.8% of the votes for a county total of 306,055 votes. 
    - Arapahoe cast 6.7% of the votes for a county total of 24,801 votes. 
- The county with the most votes was Denver
- The candidates were: 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane 
- The results were:
    - Charles Casper Stockham received 23.0% of the vote and received 85,213 votes.
    - Diana DeGette received 73.8% of the vote and received 272,892 votes. 
    - Raymon Anthony Doane received 3.1% of the vote and received 11,606 votes. 
- The winner of the election was:
    - Diana DeGette with 272,892 or 73.8% of the total votes.

The final results were printed to a file and a screen capture of that file is shown below.

![my_analysis](https://github.com/kkoehn8/Election_Analysis/blob/main/ElectionSummaryResults.PNG)

## Summary
The code that has been created for this challenge could easily be refactored and used for a vaireity of types of different election analyses. Since the raw data is provided in a csv file to use this script for different analysis we would need to be provided with a different csv file containing the new data to be analysed. Below are listed two examples of how this script could be modified and resused.

1. The script could be used for a state-wide election in any state. The code is not specific to a certain state, the script steps through the data in a provided csv file. If that file contains the same data structure (i.e. Ballot ID, County, Candidate) for another state the script could be run with few modifications except ensuring the input file is pointing to the correct data. 

2. The script could be used for different levels of government, for example, to conduct an analysis of the US Presidential Election. If the source data had columns for  Ballot ID, State, and Candidate the code could be refactored to determine the winner, how many votes they received and the percentage of votes they received. Additionally the analysis could be conducted to determine the total votes and percentage per State. If the script were to be used for this level we would want to change the reference from County to State in the script so it can be more easily read by other developers and we would need to change the terminology for our print statements. While the code may be easily refactored to conduct the analysis at the Federal level instead of the State level there could be challenges with getting all the data for a Federal election into a csv file (I'm not sure if there are row limits to a csv file). Additionally, it will probalby take much longer to run the analysis at the Federal level. I suspect we may learn better metnoed to deal with larger volumes of data later in the course.   
 
