


# Description
This application offers the ability to help determine the best applicant for a group of team members.
This application utilizes a robust web framework called FastAPI. 
Additional information and documentation can be found at https://fastapi.tiangolo.com/

When the server is running, the API is capable of taking in json input that is related to team members and various applications, and helps determine the best fit for the team by producing a score for each applicant. Routes, schemas, and additional API overview of the application can be viewed at localhost:8000/docs.

# Installation

```
pip3 install fastapi
```
```
pip3 install uvicorn
```
## To start the server:
```
uvicorn main:app --reload
```
# Endpoints
## GET /
Returns json containing data about author and purpose.

## POST /scores/ 
Input: json containing team member and applicant data

Output: json containing applicant scores
###  Sample Schema for POST request /scores
```json
{
  "team": [
    {
      "name": "string",
      "attributes": [
        {
          "intelligence": 0,
          "strength": 0,
          "endurance": 0,
          "spicyFoodTolerance": 0
        }
      ]
    }
  ],
  "applicants": [
    {
      "name": "string",
      "attributes": [
        {
          "intelligence": 0,
          "strength": 0,
          "endurance": 0,
          "spicyFoodTolerance": 0
        }
      ]
    }
  ]
}
```
### POST Response Schema
```json
{
	"scoredApplicants": [{
		"name": "string",
		"score": 0
	}, {
		"name": "string",
		"score": 0.9
	}, {
		"name": "string",
		"score": 0
	}, {
		"name": "Timmy",
		"score": 0
	}]
}
```


# Testing
Must have Pytest installed to run available tests!!
```
pip3 install pytest
```
In src directory
```
pytest
```
