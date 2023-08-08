import pywhatkit as pwk
try:
    
    pwk.sendwhatmsg("+49xxxxxxxxxxxxx", "Hi, Shaaaaaaam come here please", 17, 20)
    print("Message Sent!")
except:
    print("Error in sending the message")
