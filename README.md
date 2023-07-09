# Resume-Rater-Engine

The Resume-Rater-Engine is a robust solution that leverages the power of artificial intelligence and machine learning to streamline the recruitment process. It creates, categorizes, and scores resumes based on employer queries and job descriptions.

## Workflow:

1. **Resume Creation**: Use ChatGPT to generate at least 66 unique resumes.

2. **Data Extraction**: Parse the generated resumes to extract valuable data such as skills list, job experience, among others.

3. **Data Storage**: Store the extracted data in VectorDB, including the entire resume, skills list, and job experience.

4. **Advanced Search and Ranking**: Allow employers to provide a rubric or assign weights to prioritize certain skills, and then rank resumes based on this input. The ranking system will search the entire resume or specific sections for matching skills.

5. **Deployment**: Explore the option of deploying the solution in a Streamlit application.

## Future Enhancements:

The vision is to evolve this project into a comprehensive data engineering product with the following enhancements:

1. **Resume Submission and Storage**: Allow individuals to submit resumes directly to employers and store these resumes in the cloud.

2. **Batch Processing**: Implement batch processing with AWS Lambda function or Airflow.

3. **Employer Interface**: Enable employers to interact with this resume database through several processes described below.

4. **Knowledge Graph Integration with Neo4j**: Utilize a knowledge graph to connect diverse pieces of information in the resume database. This will enable more advanced search capabilities, such as finding the shortest distance between skillsets or using graph embeddings to map similarities among resumes.

5. **AI Filtering**: Employers can specify a requirement (e.g., a particular skill), and the system will provide a list of candidates who meet that requirement.

6. **AI Scoring**: Allow employers to input their job description and provide a score for each resume. This score will assist employers during the hiring process.

### Note: 

"Bullshit skills" like "Critical Thinking", "Scrum/agile methodology" are regarded as less concrete compared to technical skills like knowledge of specific programming languages or tools. These "soft skills" might be less useful when distinguishing among highly technical roles. However, this does not disregard their value in the broader context of job performance.
