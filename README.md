# JAP
JAP or job application platform as a medium to connect organizations with job applicants.
This program will processed the resume files and calculate the relevancy from the skills of the 
applicant to the skills required of each position and filter questions then sent a question suggestion list
to the organization admin to select the appropriate questions for that applicant.

How to run the program

Run each python files separately.

Create the following directories in the directories Filesys where the python code files are. 
This will act as the place to hold the files once it is processed.
1. ApplicantFolder
2. InboundResume
3. InboundTesseract
4. Scores
5. TempStation
6. TxtMapCleaned
7. TxtMapUncleaned
8. TxtQuesCleaned
9. TxtQuesImage
10. TxtQuesUncleaned

The code will extract the text twice, one using PDFminer and the other using Pytessaract.
Then each of the text files that were extracted will then trigger the set of codes to starts:
1. Extract skills then map with all available position and calculate the percentage match
2. Locate the text section from key words in header list then extract skills
   group the skills into difficulty levels then map with the existed question in database