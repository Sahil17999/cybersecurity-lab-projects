
import crypt

shadow = "alice:$6$jJ70WFelxvD_wRqJ$da5a71a994d6305665706242af8cbea84fc963d126f11ba44129c35d640161401b9b1174e09a6f1840227821477f5445a33e4af43ade0b3a6adaecb388f7308c:19447:0:99999:7:::"

target_hash = shadow.split(":")[1]

salt = "$6$" + target_hash.split("$")[2] + "$"

print("Salt:", salt)
print("Target Hash:", target_hash)

with open("months.txt", "r", encoding="utf-8", errors="ignore") as f:
	for line in f:

		password = line.strip()
	
		shadow_can = crypt.crypt(password, salt)

		print("Trying pwds", password)

		
		#compare only the password portion of the shadow file
		if shadow_can == target_hash:
			print("Password Found:", password)
			break
