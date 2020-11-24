# Utilities to be used for main.py
# Logic to score applicants from POST Request

# Parameters: List of team members, and list of applicants
# Returns the applicants scores in json
# Driver function
def score_applicants(team_members, applicants): 
    team_average = get_team_average(team_members)    
    applicant_scores = get_applicant_scores(applicants,team_average)

    return applicant_scores

# Parameter: list of team members
# Returns Value: The team's average score
# Averages the team's score against 40 total points
def get_team_average(team_members):
    team_total = 0 

    for member in team_members:
        attr = member.attributes[0]
        team_total += attr.intelligence + attr.strength + attr.endurance + attr.spicyFoodTolerance

    team_average  = team_total / (40 * len(team_members))

    return team_average

# Parameters: list of applicants, average score from team members
# Return Value: applicant_scores in json
# Scores applicant based on team's average score
def get_applicant_scores(applicants,team_average):
    applicant_scores =  []

    for applicant in applicants:
        attr = applicant.attributes[0]
        average = (attr.intelligence + attr.strength + attr.endurance + attr.spicyFoodTolerance) / 40
        score = round(average / team_average,2)

        # Keep them humble, range [0,1]
        if score >= 1:
            score = .99

        applicant_scores.append({"name": applicant.name,"score": score})

    return applicant_scores


