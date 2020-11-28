import praw

reddit = praw.Reddit(client_id="****",
    client_secret="****",
    username="****",
    password="****",
    user_agent="****")

while True:
    score = submission.score
    awards = len(submission.all_awardings)
    ratio = submission.upvote_ratio
    upvotes = round((ratio*score)/(2*ratio-1)) if ratio != 0.5 else round(score/2)
    downvotes = upvotes-score
    edited = f"{str(upvotes)} upvotes,\n\n{str(downvotes)} downvotes,\n\n{str(submission.num_comments)} comments, \n\n{score} score,\n\nand {awards} awards!"
    submission.edit(edited)
    
