##################### solution with function ############
def majority_vote(lst):
    most_voted = max(lst, key=lst.count)
    vote_count = lst.count(most_voted)

    print(f"The most voted is {most_voted} with {vote_count} vote count ")

majority_vote(["A", "B", "B", "B", "C", "A"])

############### solution without function ############

majority_vote = ["A", "B", "B", "B", "C", "A"]

most_voted = max(majority_vote, key=majority_vote.count)
vote_count = majority_vote.count(most_voted)

print(f"The most voted is {most_voted} with {vote_count} vote count ")



