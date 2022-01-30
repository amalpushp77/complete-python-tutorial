"""
    Python Lists Coding Exercise
Given that on line 2, you have access to a List called scores that contains a bunch of whole numbers ordered randomly.
On line 3, we've created a variable called top_scores
which contains an empty List.
Write some code to create a new List that has the top 3 highest scores from the List of scores and assign that List to
top_scores.
e.g. It scores = [43, 12, 6, 78, 2, 14]
After your code is executed, the variable' top_scores I should equal  [78, 43, 14] .
"""


def top_three(scores):
    scores = scores
    top_scores = []

    minimum_score = 0
    for i in scores:
        if len(top_scores) < 3:
            top_scores.append(i)
            minimum_score = min(top_scores)
        else:
            if i > minimum_score:
                top_scores.remove(minimum_score)
                top_scores.append(i)
                minimum_score = min(top_scores)

    # Leave this line alone
    return top_scores


print(top_three([540, 57, 12, 45, 87, 77, 98, 101]))
