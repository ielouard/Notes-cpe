from flask import Flask
from parse import getNotes
import filecmp
import time
import fbchat

app=Flask(__name__)

@app.route('/')
def index():
	client = fbchat.Client("chatbotcpe@gmail.com", "CPE-Lyon2016") # Identifiant facebook
	friends = client.getUsers("Ibrahim El Ouard")  # Personnes à qui tu veux envoyer le message
	friend = friends[0]
	getNotes("parse.txt") 
	getNotes("parse2.txt")

	while(filecmp.cmp('parse.txt','parse2.txt')==True):
		print("pas encore de nouvelles notes")
		sent = client.send(friend.uid, "pas encore de nouvelles notes")
		time.sleep(3600) # Attendre 1h
		getNotes("parse2.txt")

	
	sent = client.send(friend.uid, "des notes sont sorties")

if __name__ == "__main__":
	app.run()