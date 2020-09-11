# Election_Analysis

## Project Overview
A Colorado board of election employees needs the following information to complete the election audit of a recent local congressional election

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calulated the total number of votes for each candidate
4. Calculate the percentage of votes for each candidate
5. Determine the winner of the election based on popular votes
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout

## Resources
- Data source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code Version 1.48.2

## Results
The Analysis of the election shows that:

- There were 369,711 votes cast in the election
- The county results were:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- Denver county had the largest number of votes (306,055)
 - The candidate results were:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was Dianne DeGette who got 73.8% of the vote and 272,892 votes

## Summary
The report was produced from the python script PyPoll_Challenge_starter_code.py
The dataset election_results.csv used in this report had the following comma separated fields
    Ballot ID,County,Candidate

The script uses only the County and Candidate fields

The same script can be modified to produce similar results with other datasets

Example 1: Assuming that our new dataset contains the state information in place of county as below
    Ballot ID,State,Candidate

We can keep everything the same and just replace the "County" with "State" in lines 94 and 125

Example 2: Additionaly if our new data set was using pipe delimited fields as below
    Ballot ID|State|Candidate

We could simply modify the line 39 and specify the delimiter
    file_reader = csv.reader(election_data,delimiter='|')