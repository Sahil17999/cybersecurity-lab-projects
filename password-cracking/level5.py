
import hashlib

target_hash = "a0b629570a31f7e3e377d8eba828e414"

with open("months.txt", "r", encoding="utf-8", errors="ignore") as f:
	for line in f:

		password = line.strip()
	
		md5_hash = hashlib.md5(password.encode()).hexdigest()

		
		print(password, md5_hash)
		if md5_hash == target_hash:
			print("Password Found:", password)
			break