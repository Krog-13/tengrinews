from post import Tengri
from comment import Comment
from sqlliter import SQLiter

# initialisation DB
db = SQLiter('tengrinews')

# initialisation class Tengri
tengri = Tengri()
comments = Comment()
# get new links
new_links = tengri.get_links()

# get last add in db link
last_link = db.get_last_link()

#check new post is?
def check_last():
    '''Check new post in tingrinews.kz'''
    step = 0
    if last_link:
        for i in new_links:
            if int(last_link[0][-7:-1]) == int(i[-7:-1]):
                break
            else:
                step += 1
    else:
        step = 15
    return step

step = check_last()
print(step)
# get full data
info = tengri.get_post(new_links[:5])
#add in db new info
db.add_post(info)

#add comments in posts
id_and_links = db.get_link_for_comment(2)
print('selenium')
data_of_comments = comments.get_comments(id_and_links)
#add comment in db
db.add_comment(data_of_comments)




