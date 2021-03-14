#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This software is free to use, distribute and modify.  MIT License terms in the 'LICENSE.txt' file. 


# In[ ]:


# We need to use two things that are elsewhere.  This cell imports them so that we can ask the software to do some randomization and some time-based stuff.
import random, time


# In[ ]:


# These are the word lists we'll use.  
# Edit these to your heart's content, paying attention to the quotation marks, and the requisite comma after each entry. Square brackets on the ends. 

word_1 = ["Anacronistic","Future","Setup","Relatable","Quiet","Recumbant","Moon","Monster","Pizza","Business","Ocean", "Shrimp","Telescopic","Resiliency","Brutalist","Cheeseboard","Bear","Future","Clump","Oversized","Conflicting","Curbside","Secret","Somatosensory","Realistic","Psychic","Expensive","Moustache","Krill","Badger","Surprise","Novelty","Plant","Izmuth","Thought","Technicolor","Grin","Socialist","Attractiveness","Sky","Juice","Luxury","Canadian","Space","Witch","Landing","Apocalytic","Corona","Viral","Emotional","Vintage","Gen-X","Surprise","Homeopathic","Liver","Pungent","Emotional","Computer","Murky","Performance","Hyperbolic","Moral","Vortex","Dark","Aesthetic","Recalcitrant","Fictive","Therapuetic","Chaos","Brain","Theoretical","Pleasure","Roof","Vegan","Misdemeanor","Business","Pear","Accusation","Death","Feed","Mars","Sexo-spiritually","Experimental","Amplified","Dream","Scientific","Faith","Glittery","Millipede","Child","Fiona","Grievous","Horseshoe","Diplomacy","Sky","Dog","Apology","Miscellaneous","Loudness","Emotional","Soft","Gooey","Glove","Plain","Metaphorical","Antibacterial","Fecal","Apollo","Assassain","Worm","Severe","Disaster","Vibrant","Fusion","Millenial","Peacetime","Tong","Snork","Horn","Scoby","Basement","Hypothetical","Guilt","Phantom","Recreational","Heavy-Duty","Wizard","Proverbial","Dusk","Timeless",]
word_2 = ["Vernacular","Basic","Wizard","Mystique","Mysticism","Replendance","Germs","Dad","Uncle","Podcast","Master","Jesus","Dawg","Peistalisis","Expert","Apologist","Culture","Contingency","Itchy","Noise","Mythology","Vegans","Growler","Silence","Stretching","Testicle","Starvation","Smell","Sighs","Tickler","Alcatraz","Fragrence","Hazmat","Lazerus","Christmas","Leader","Yawn","Diesel","Coupons","Nuisance","Noodz","Library","Beats","Innovation","Herpes","Prison","Claw","Decor","Celibate","Nuns","Espionage","Credenza","Denizen","Chores","Coffee","Reading","Prose","Substratum","Freaks","Apocrapha","Velvet","Scent","Turpitute","Action","Heather","Cultivation","Municipality","Kinship","Nihlism","Defrost","Twizzler","Superstar","Garden","Hooch","Recliner","Statistics","Goose","Curse","Finger","Fiber","Horns","Gandhi","Itchy","Striptease","Reality","Microwave","Water","Suplex","Splendor","Neutrality","Gradient","Premium","Pangolin","Camelot","Crab","Jazz","Lab","Present","Anxiety","Creep","Firehose","Condor","Morrow","Modernization","Soup","Rampage","Melon","Plume","Mutations","Couture","Drive","Nudity","Peril","Grey","Leftovers","Expert","Codpiece","Candy","Hole","Paradox","Meathook","Cheeseknife","Fellatio","Consultant","Power","Mathmatics","Delicates","Edgelord","Gatekeepers","Birds","Chad",]


# In[ ]:


# This is a simple function that just picks an item off of each list at random, returns them CAPITALIZED as the variable "both". 
# It won't do anything until we "call" it later. 
def nameGenerator(): 
    first = random.choice(word_1)
    second = random.choice(word_2)
    both = first.upper() +" " + second.upper()
    
    return both


# In[ ]:


# I think it's more fun to make people wait a sec.  So we'll make a second function here that just makes a fake loading bar
#'duration' is a parameter we'll give the function, that lets us tell the bar how long to complete. 
# remember that this won't do anything until we "call" it later. 
# This is, by far, the most complicated thing in this program. 

def loadingBar(duration):  
    # how many chunks should our loading bar have? 
    total_length = 40
    
    #currently empty variable that will hold our loading bar.
    progress = ""
    
    #the "for loop" below will iterate the number of times that we've defined above as "total_length"
    for i in range(total_length): 
        
        #add an asterisk to the "progress" variable. 
        progress += "*"
    
        #print the current state of the "progress" variable.  
        #The "\r" means that we should re-write the current line of the output, instead of generating a new line for each running of the loop
        print(progress, end="\r"),
        
        # Now, we'll wait for just a moment before repeating the loop. This is called "sleeping". 
        # we can calculate the needed sleep time by divding the "duration" by the "total_length".  
        #We haven't actually told it how much of a duration (in seconds) yet, but we'll do that when we call this function. 
        time.sleep(duration/total_length)
        
    #now repeat the loop!         


# In[ ]:


# if you remove the "#" on the next line and run this cell, you can try out a five second loading bar :) 
#loadingBar(5)


# In[ ]:


# You'll need to run this cell each time you want to get a new band/song name. 

# Let's name our band by running nameGenerator and saving that as the variable "band_name".  Let's "call" nameGenerator. 
band_name = nameGenerator()

# Let's name our first hit single, by running nameGenerator again and saving it as a different variable. 
song_name = nameGenerator()



# In[ ]:


# Great, we've got everything we need.  Now it's just time to make the output look pretty. 

print("BandGen: A highly good band and song name generator")
print("©2021 Jeff Emtman. V1.0 - MIT License")

#time for some quick loading bars! 
print("\nVarigating Inputs...")
loadingBar(1)
print("\nCrushing Self-Doubt...")
loadingBar(.75)
print("\nSuccess!")

time.sleep(1)
print("\n\n")

print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")
print(song_name, "by", band_name)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")

#final output below. 

input("\n\npress 'enter' to quit   ")
