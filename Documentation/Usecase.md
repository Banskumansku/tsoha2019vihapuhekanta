# What do? Case of adding a tweet
User sees a mean tweet and wants to make the world a better place by making hatespeech detection algorithms better
User adds tweet id to the tweet id section, marks whether or not it's hateful or just offensive
The background process retrieves the tweet data and adds it to the db row

# How do? Case of seeing and searching the tweets user has posted
Admin wants to search for tweets with particular words in it
Admin selects whether to search by type or text
Admin chooses from dropdown and writes down query
Admin is shown the results of query

# How do? Case of deleting a tweet
User doesn't want the tweet to be in DB anymore
User searches for tweet
From query results user presses delete button
Entry is deleted

# How do? Admin functionality
Where the normal user can only see their own tweets, the admin can see the listing of all tweets, search, delete and edit all tweets. 
Admin can also see the logs of every event in the system

# How do? Extended admin functionality
At the moment only admin can delete accounts from auth/users, under time constraints it wasn't added to every user

# How to? Downloading DB (To be made)
User can select the "Download" option to receive the entire DB in a cvs format

# How to? Delete own account (to be made)
Go to account information and select delete account

#How to? Change user password (to be made)
Go to account information and select change password
Be taken to change password screen and be made to write it out twice