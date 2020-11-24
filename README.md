---
---
# Description
This application utilizes a robust web framework called FastAPI. 
Additional information and documentation can be found at the following: https://fastapi.tiangolo.com/

When the server is running, the API offers the ability to help determine the best applicant for a team.
Routes,JSON schemas and addiontal API overview of the application, can be viewed at ***localhost:8000/docs***.

The server listens on port:8000 and outputs as a standard API. 
---
# Installation
In the project's home directory, run the following:

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

#  Sample Schema for POST request /scores
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
### POST Response
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
