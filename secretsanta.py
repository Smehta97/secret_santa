import random
import smtplib

class Person:
    give_ID = 0
    take = False
    def __init__(self, name, email, per_ID):
        self.name = name
        self.email = email
        self.id = per_ID
    def displayPerson(self):
        print "Name: ", self.name, "|| E-Mail: ", self.email, "|| ID: ", self.id, "|| give_ID: ", self.give_ID

ID_count = 0

def addPerson(name, email, persons):
    global ID_count
    obj = Person(name, email, ID_count)
    persons.append(obj)
    ID_count += 1

def make_santa(persons):
    length = len(persons)
    allowed_values = list(range(0, length))
    print "current values: ", allowed_values
    for i in range(0, length):
        while True:
            num = random.choice(allowed_values)
            if(num != i):
                break
            if(length == 1 and num == i):
                print "Elves screwed up. Recomputing."
                make_santa(persons)
                break

        print persons[i].name, ": ", i, "|| num: ", num
        persons[i].give_ID = persons[num].id
        persons[num].taken = True
        allowed_values.remove(num)
        print "updated values: ", allowed_values

def main():
    persons = []
    print "\nType h for help\n"
    while True:
        choice = raw_input("> ")
        choice = choice.lower() #Convert input to "lowercase"

        if choice == 'h':
            print("c: to continue adding people\nexit: to quit\nprint: to show list\nsantify: to draw secret santas\nsend: to send secret emails")

        if choice == 'exit':
            print "Merry Christmas!"
            break

        if choice == 'print':
            for person in persons:
                person.displayPerson()

        if choice == 'santify':
            make_santa(persons)

        if choice == 'c':
            nameInp = raw_input("Name: ")
            emailInp = raw_input("Email: ")
            addPerson(nameInp, emailInp, persons)

        if choice == 'send':
            if len(persons) < 2:
                print "Not enough people"
            for i in persons:
                if not i.taken:
                    print("Person", i.name, "not taken")
                    break
            print "Sending Emails..."
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("secretsanta.jacobs@gmail.com", "123Digga")
            for person in persons:
                print "Sending Email to " + person.name
                message = "\r\n".join([
                  "From: secretsanta.jacobs@gmail.com",
                  "To: " + str(person.email),
                  "Subject: Ho Ho Ho!",
                  "",
                  "Dear Santa " + str(person.name) + ",\n\nYou're the secret santa to " + str(persons[person.give_ID].name) + "!\nSpending limit is 20 euros\n\nHappy shopping!"
                  ])
                server.sendmail("secretsanta.jacobs@gmail.com", person.email, message)
            print "Sending success"
            server.close()

if __name__ == '__main__':
    main()
