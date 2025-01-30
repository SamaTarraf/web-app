import bcrypt

password = "firstUser123"
#hashed_password = bcrypt.hashpw("FirstUser123".encode(), bcrypt.gensalt())

print(bcrypt.checkpw(password.encode(), "$2b$12$76Kd7MEpN8dz2./mS.JNru9Uo/O2v5aTplzMWWFPtT6ViVAw0SEsu".encode()))