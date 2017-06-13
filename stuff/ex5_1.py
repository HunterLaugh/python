# coding: utf-8
# more about variable    format print  string
# use  %s for string
# use  %d for integer

name='Zed A Shaw'
age=35   #not a lie
height=74 #inches
weight=180 #lbs
eyes='Blue'
teeth='White'
hair='Brown'

print("Let's talk about %s." % name)
print("He's %d inches or %.2f cm tall." % (height,height*2.54))
print("He's %d pounds or %.2f kg heavy." % (weight,weight*0.45))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(eyes,hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." %(age,height,weight,age+height+weight))