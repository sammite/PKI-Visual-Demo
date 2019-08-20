# This is meant to be used for a demonstration of PKI, by having a user
# input one code to "open" a safe, and a separate code to close.
# I don't have time or the place to do it right now, but my hope is to eventually
# rig a raspberry pi to actually work a lock in this manner, and use that to
# visually demonstrate how Public and private keys work.


#Passwords
unlock = "P@ssword"
lock = "hunter2"


# define a function for opening/closing the box

open_box = "the box is open"
closed_box = "the box is closed"
box_state = closed_box


def openpassword_checker():
    global box_state
    boxlock = box_state
    print "Type the password to open the box. Currently %s" % boxlock

    checkpass = raw_input("> ")

    if checkpass == unlock:
        box_state = open_box
    else:
        print "sorry, try again."

def closepassword_checker():
    global box_state
    boxlock = box_state
    print "Type the password to lock the box. Currently %s" % boxlock

    checkpass = raw_input("> ")

    if checkpass == lock:
        box_state = closed_box
    else:
        print "sorry, try again."

while 1 == 1:
    if box_state == closed_box:
        openpassword_checker()
    elif box_state == open_box:
        closepassword_checker()
    else:
        print "we're sorry, your call could not be completed as dialed."
        box_state = closed_box
