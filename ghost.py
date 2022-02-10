import amino

client = amino.Client()
client.login(email="tdqspy@1secmail.com", password="raviji11")

print("\nlogged in...")
n=input("\nChat Link:")

fok=client.get_from_code(n)
id=client.get_from_code(n).objectId
cid=fok.path[1:fok.path.index("/")]
print(cid)
client.join_community(cid)
subclient=amino.SubClient(comId=cid,profile=client.profile)
print("\nJoined Community....")
subclient.join_chat(chatId=id)
while True:
     mssg=input ("\n>> ")
     subclient.send_message(chatId=id,message=mssg,messageType=109)
     print("\nMessage Send Succesfully....")
