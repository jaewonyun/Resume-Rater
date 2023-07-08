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


## Concept #1
Employer: "Filter all candidates with X"
Assistant: "Sure, here are the list of candidates with requirement X?
- 
-  

## Concept #2
Employer enter their job description
Gives score(s) for each resume
Then employer can use the scores for hiring

## Concept #3
Employer gives rubric, or weights to emphasize skills. 
### Example
Essential: AWS, SQL, python
Nice-to-have: Scala, ....

JS = [skill_1, skill_2, ...]
W = [w1, w2, .... 0.1]
CS = [0,  ....    R]

dot(W, CS) = score 
norm_score = 5*score/max(score)