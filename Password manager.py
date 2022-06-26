pwd = input("What is the master password? ")

def view():
      with open('passwords.txt', 'r')as f:
        for line in f.readlines():
            data =line.rstrip()
            user, passw = data.split("|")

            print("User:", user, "| Password:",passw)
    



def add():
     name = input ('Account Name: ')
     pwd = input("Password: ")

     with open('passwords.txt', 'a')as f:
        f.write(name + "|" + pwd +  "\n")


while True:
    mode = input(
      "would you like to add a new password or view existing ones(view, add),press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
      pass
      view ()
    elif mode == "add":
       pass
       add()
    else:
       print("Invalid mode.")
       continue