#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Mail Merge Project Start/Input/Names/invited_names.txt", mode='r') as file:
    invitees = file.readlines()
    for name in invitees:
        with open("Mail Merge Project Start/Input/Letters/starting_letter.txt", mode='r') as files:
            letter = files.read()
            name = name.strip()
            letter = letter.replace("[name]", name)
            with open(f"Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode='w') as done:
                done.write(letter)
