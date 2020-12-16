import pyttsx3
friend = pyttsx3.init()
speech = input("say something: ")
friend.say(speech)
#friend.say("You are dashing smart . Emon .  I  miss you!")
friend.runAndWait()