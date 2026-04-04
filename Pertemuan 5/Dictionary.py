#membuat struktur data dictionary
userLogin = {"name": "Fadrial keche", "age":19, "role":"sundae"}
print(type(userLogin))
# Mengakses Data

print(f"Nama Akun : {userLogin['name']}")
print(f"Umur Akun : {userLogin['age']} Tahun")
print(f"Role Akun : {userLogin['role']}")

#akses data seluruh
print(userLogin.items())
print(userLogin.keys())
print(userLogin.values())

# Menambah Data kedalam dictionary big-O O(1)
userLogin["email"] = "paddrell.me@gmail.com"
print(userLogin)

# Menghapus Data dari dictionary big-O O(1)
userLogin.pop("age")
print(userLogin)

#mengubah data dalam dictionary big-O O(1)
userLogin["role"] = "jawaan"
print(userLogin)

#nested dictionary
dbUser = {"user1": {"name": "Fadrial", "age": 18, "role": "Orang Ganteng"},
          "user2": {"name": "Padrell", "age": 19, "role": "raja sunda"},
          "user3": {"name": "Jp", "age": 20, "role": "sunda pisan"}}

print(dbUser)

#akses value base key
print(dbUser["user1"])

#melakukan pencarian data dalam dictionary
finword = input("Masukkan nama user yang ingin dicari: ")
if finword in dbUser:
    print("Data ditemukan")
    print(dbUser[finword])
else:
    print("Data tidak ditemukan")