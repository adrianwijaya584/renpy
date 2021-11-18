# The script of the game goes in this file.
define hor= Character("HOR", color="#ababab")
define nyalter= Character("Nyalter")

# The game starts here.

label start:
    "In 2021 there's a young boy who try to learn renpy"
    "Well this is his first game, let's see how it's going"

label sprites:
    scene bg 1
    show hor happy
    hor "Hello i'm bronya nice to meet you"
    hor "Do you want to know more about me ?"
menu:
 "yes":
  jump choices1_a
 "no":
  jump choices1_b

label choices1_a:
 hor "yes, i'm feeling happy"
 hor "need to add1"
 hor "need to add2"
 hor "need to add3"
 jump choices1_common
 
label choices1_b:
  hide bg 1
  hor "well then, bye"
  jump choices1_common

label choices1_common:
 "nice !."

label end:
 hide hor happy
 "that's the end of the game. Bye"