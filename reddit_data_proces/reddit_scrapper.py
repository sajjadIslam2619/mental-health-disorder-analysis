import praw
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Read variables
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')
username = os.getenv('REDDIT_USERNAME')
password = os.getenv('REDDIT_PASSWORD')

# Initialize PRAW with env variables
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

# Verify the connection
try:
    user = reddit.user.me()
    if user:
        print(f"Authenticated as: {user}")
    else:
        print("Authentication failed. Please check your credentials.")
except Exception as e:
    print(f"An error occurred: {e}")

# Access the subreddit
subreddit = reddit.subreddit('OpiatesRecovery')

# Function to fetch comments based on the provided method
def get_comments(submission, comment_sort='top', limit=3):
    submission.comment_sort = comment_sort
    submission.comments.replace_more(limit=0)
    comments = submission.comments[:limit]
    if not comments:
        return [{
            'comment_author': '',
            'comment_body': '',
            'comment_ups': '',
            'comment_downs': '',
            'comment_score': ''
        }]
    return [{
        'comment_author': comment.author.name if comment.author else '[deleted]',
        'comment_body': comment.body,
        'comment_ups': comment.ups,
        'comment_downs': comment.downs,  # Not directly available, calculated from score
        'comment_score': comment.score
    } for comment in comments]

# Function to fetch posts and save to CSV
def fetch_and_save_posts(after=None, limit=100, comment_sort='top', comments_limit=3, filename='reddit_posts_and_comments.csv'):
    posts_data = []
    
    #submissions = list(subreddit.top(limit=limit, params={'after': after}))
    #submissions = list(subreddit.rising(limit=limit, params={'after': after}))
    submissions = list(subreddit.hot(limit=limit, params={'after': after}))
    for submission in submissions:
        post_info = {
            'title': submission.title,
            'post_author': submission.author.name if submission.author else '[deleted]',
            'selftext': submission.selftext,  # Post content
            'score': submission.score,
            'ups': submission.ups,
            'downs': submission.downs,  # Not directly available, calculated from score
            'url': submission.url,
            'comments': get_comments(submission, comment_sort=comment_sort, limit=comments_limit)
        }
        posts_data.append(post_info)
    
    # Create a DataFrame
    posts_df = pd.DataFrame(posts_data)
    
    if 'comments' in posts_df.columns:
        # Expand the comments column into separate rows
        expanded_comments = posts_df.explode('comments').reset_index(drop=True)

        # Normalize the nested comment dictionaries into separate columns
        comments_df = pd.json_normalize(expanded_comments['comments'])

        # Combine the posts and comments data
        combined_df = expanded_comments.drop(columns=['comments']).join(comments_df)
    else:
        combined_df = posts_df

    # Append to a CSV file
    if not os.path.isfile(filename):
        combined_df.to_csv(filename, index=False)
    else:
        combined_df.to_csv(filename, mode='a', header=False, index=False)

    print(f"Scraping complete for {limit} posts. Data saved to '{filename}'.")

    # Return the fullname of the last submission to use as 'after' in the next call
    return submissions[-1].fullname if submissions else None

# Fetch top 1000 posts in batches of 100, with rate limiting
batch_size = 100
total_posts = 1000
after = None

for _ in range(0, total_posts, batch_size):
    after = fetch_and_save_posts(after=after, limit=batch_size, comment_sort='best', comments_limit=3, filename='reddit_hot_posts_and_best_comments_with_author.csv')
    print(f"Fetched {batch_size} posts. Waiting to avoid rate limit...")
    time.sleep(30)  # Pause to respect rate limits (adjust as needed)

print("All posts have been scraped and saved.")