import random
import smtplib
import sys

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
    print "Santifying!\n"
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

        persons[i].give_ID = persons[num].id
        persons[num].take = True
        allowed_values.remove(num)

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
            emailInp = raw_input("Username: ")
            addPerson(nameInp, (emailInp + "@jacobs-university.de"), persons)

        if choice == 'e':
            print "People list:"
            for person in persons:
                print person.id, ": ", person.name
            search = raw_input("ID: ")
            p_edit = persons[int(search)]
            n_edit = raw_input("New name: ")
            e_edit = raw_input("New username: ")
            persons[int(search)].name = n_edit
            persons[int(search)].email = e_edit + "@jacobs-university.de"

        if choice == 'r':
            print "Rigging Terminal"
            print "Select two people"
            for person in persons:
                print person.id, ": ", person.name
            n = int(raw_input("to give: "))
            m = int(raw_input("to whom: "))

            has = 0
            for x in persons:
                if x.give_ID == persons[n].id:
                    has = x.id

            temp = persons[has].give_ID
            persons[has].give_ID = persons[m].give_ID
            persons[m].give_ID = temp

        if choice == 'send':
            if len(persons) < 2:
                print "Not enough people"
            for i in persons:
                if not i.take:
                    print("Person ", i.name, " not taken")
                    sys.exit()
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
                  "There once was a fam,\ntiempo es muy frio\nwhere da presents at?\n\nDear Santa " + str(person.name) + ",\n\nYou're the secret santa to " + str(persons[person.give_ID].name) + "!\nSpending limit is 20 euros\nBe ready by 16th of December!\n\nHappy shopping!"
                  ])
                server.sendmail("secretsanta.jacobs@gmail.com", person.email, message)
            print "Sending success"
            server.close()

if __name__ == '__main__':
    main()
