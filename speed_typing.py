import time

def speed_typing_game():
    text_to_type = "The quick brown fox jumps over the lazy dog"
    print("Type the following text as fast as you can:")
    print(text_to_type)
    
    input("Press Enter when you are ready...")
    
    start_time = time.time()
    
    user_input = input("Type here: ")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if user_input == text_to_type:
        print(f"Congratulations! You typed it correctly in {elapsed_time:.2f} seconds.")
    else:
        print("Oops! It seems there are errors in your typing. Try again.")

if __name__ == "__main__":
    speed_typing_game()

