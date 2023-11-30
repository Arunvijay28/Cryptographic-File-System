# Cryptographic-File-System
In modern days data security in very much important this project deals with the special way of encryption called symmetric key encryption technique
It can be used for:
  1) Confidential data sharing
  2) Securing personal files

# Symmetric key encryption : 
In which same key is used for both encryption and decryption in which if the key is lost the encrypted data cannot be decrypted or if the key is stolen then the person who holds the key can see the encrypted data

In python it has a cryptographyic module called Fernet in which it generates a secret key with extension as .key .Once a file is created user my specifiy their know key which can be the password for the file or the system by itself will generate the key
once the key is generated the File can be encrypted ,but foe decryption the file with same key must be sepcified if not the text cannot be decrypted and it throws invalid Fernet Token error

At present it encrypts any form of text files in future it can be extended such that it can encrypt any type of files starting from pdf,img,text etc..
