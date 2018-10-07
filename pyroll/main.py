import os
import pandas as pd



#Create vote DataFrame
voteData = pd.read_csv("election_data.csv")

#Get Total
hTotal= voteData["Voter ID"].count()

#Build Result Set.
#----Mimic a SQL GroupBy on Candidate
#----Use Htotal to get percentage
#----Sort by %, and keep dataframe.  
gCandidate= voteData.groupby("Candidate")
gCandidatesVotes= gCandidate.size().reset_index(name='Votes')
gCandidatesVotes["%"] = (gCandidatesVotes['Votes'] / hTotal)*100
gResults=gCandidatesVotes.sort_values(by="%",ascending=False)



#Print results to Screen
print("\n\nVoting Results")
print("______________________________________________________")
print (f'Total Votes:  {hTotal}')
print("______________________________________________________\n")
print (gResults.to_string(index=False))
print("______________________________________________________")
print(f'The Winner is: {gResults.at[gResults["%"].idxmax(),"Candidate"]}  ')


#Print results to file
ToFile= open("GlennResults.txt","w+")

ToFile.write("Voting Results\r\n")
ToFile.write("______________________________________________________\r\n")
ToFile.write (f'Total Votes:  {hTotal}\r\n')
ToFile.write("______________________________________________________\r\n")
ToFile.write (gResults.to_string(index=False))
ToFile.write("\r\n______________________________________________________\r\n")
ToFile.write(f'The Winner is: {gResults.at[gResults["%"].idxmax(),"Candidate"]} \r\n ')

ToFile.close()
