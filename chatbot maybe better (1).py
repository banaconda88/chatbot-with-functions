#!/usr/bin/env python
# coding: utf-8

# In[3]:


def greeting():
    name = input("Hello, what is your name.")
    print("Hello", name)

def quality():
    smt = input("How's your day been going")
    day = smt.lower()
    if day == "horrible":
        print("If your day at rock bottom then it can only get better.")
    elif day == "bad":
        print("At least your day isn't doing horrible, just do something your enjoy.")
    elif day == "fine":
        print("At least your day hasn't been going bad.")
    elif day == "good":
        print("That's good, keep working at yur day to make it even better.")
    elif day == "great":
        print("If your day has been doing so good, then try to avoid doing anything that would ruin you.")
    else:
        print("If your day is only" , day, "then try to make it even better.")
        
def show():
    sho = input("Do you have any shows that you'd recommend to this bot and its creator?")
    show = sho.lower()
    if show == "kimetsu no yaiba" or show == "demon slayer":
        print("My creator also very much likes to watch demon slayer, although he is sad about having to wait for the movie.")
    elif show == "seven deadly sins" or show == "nanatsu no taizai" or show == "the seven deadly sins":
        print("That is actually my creator's most favorite show and anime that he has ever seen.")
    else:
        print("I've never heard of", show, "before, I'll tell my creator to watch it.")

def fav_food():
    foo = input("What is your favorite food?")
    food = foo.lower()
    if food == "lasagna":
        print("Oh, you have the same taste as my creator when he was younger.")
    elif food == "curry":
        print("Oh, you share the same tastes as my creator and he approves of your choice.")
    elif food == "icecream" or food == "ice cream":
        print("Oh, my creator also really likes ice cream, especially on hot days. But the popsicles resembling cartoon characters look very sad in my opinion.")
    else:
        print("Oh I have not heard of", food, "before, I'll tell my creator to try it.")
def chatbot():
    greeting()
    quality()
    show()
    fav_food()
    print("Well that concludes my functions, so this is goodbye. It was fun talking to you.")
    
chatbot()


# In[ ]:




