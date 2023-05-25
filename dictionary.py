#Exercise 1: Make a dictionary which has 7 animals and the sounds that they make.

animalsounds = {"cow":"moo", "pig":"oink", "sheep": "baa", "dog":"bark", "cat":"meow", "bee": "buzz"}


for i in animalsounds.keys():
    print(i, animalsounds[i])
    
animalsounds["cat"] = "purr"
animalsounds["lion"] = "roar"

animalsounds.pop ("cat")
print(animalsounds)