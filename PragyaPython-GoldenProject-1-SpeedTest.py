#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

def speed_typing_test():
    words = [
        'python', 'programming', 'language', 'computer', 'keyboard',
        'code', 'typing', 'practice', 'speed', 'accuracy', 'challenge'
    ]
    
    print("Welcome to the Speed Typing Test!")
    print("You will be presented with random words to type.")
    print("Type each word and press Enter to continue.")
    input("Press Enter to start...")
    
    random.shuffle(words)
    start_time = time.time()
    
    for word in words:
        print(f"\nType the word: '{word}'")
        user_input = input().strip()
        
        while user_input != word:
            print("Incorrect. Try again.")
            user_input = input().strip()
            
        print("Correct!")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60
    words_typed = len(words)
    wpm = words_typed / minutes
    
    print("\nTest complete!")
    print(f"You typed {words_typed} words in {minutes:.2f} minutes.")
    print(f"Your typing speed is approximately {wpm:.2f} words per minute.")

# Run the speed typing test
speed_typing_test()


# In[ ]:




