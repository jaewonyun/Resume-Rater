# Resume-Rater-Engine

1. Create at least 100 resumes from ChatGPT - Jae

2. Extract from resumes - John/Jae 
 --> skills list
 --> job experience
 --> whatever else...

3. Put them all in vectordb - John (Chroma)
 - whole resume
 - skill list
 - job experience

4. Perform similarity search based on employer query
- rank or score resumes with concepts below

5. Deploy in streamlit app???

6. Beyond the hackathon demo (data engineering product)
- people send resume to employer, store resumes in cloud
- batch processing, with AWS lambda fn or Airflow
- allow employers to use this database via different processes below


## Concept #1
Employer: "Filter all candidates with X"
Assistant: "Sure, here are the list of candidates with requirement X?
~~ Pandas or SQL agent

## Concept #2
Employer enter their job description
Gives score(s) for each resume
Then employer can use the scores for hiring

## Concept #3
Employer gives rubric, or weights to emphasize skills. 
### Example
Essential: AWS, SQL, python
Nice-to-have: Scala, ....

Make a long list of all possible tech skills --> 100
our vectors have to be 100 dim
- Programming language
- Cloud
- Tools: Analytics, ML, DL, 

Bullshit skills: "Critical thinking", "Scrum/agile methodology"

JS = [skill_1, skill_2, ...]
W = [w1, w2, .... 0.1]
CS = [0,  ....    R]

Employer input:
skills : [s1, s2, s3 ... ]
weights : [w1, w2, w3 ... ]

search entire resume for matching skills
OR search only job experience for matching skills

dot(W, CS) = score 
norm_score = 5*score/max(score)