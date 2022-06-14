import random
import string
# to monitor the time taken by the program
import timeit
def generate(strlen):
    alphabet = string.ascii_lowercase + ' '
    sentence = ''
    for j in range(strlen):
        sentence += random.choice(alphabet)
        # i = random.randrange(27)
        # or sentence += alphabet[i]
        j += 1
    # or sentence = "".join(random.choice(alphabet)) for _ in range(strlen)
    return sentence

def score(desired_sentence, sentence):
    num_common = 0
    for i in range(len(desired_sentence)):
        if desired_sentence[i] == sentence[i]:
            num_common+=1
        i +=1
    
    percentage_common = int((num_common/29)*100)
    return percentage_common

def main():
    lenStr = 28
    shakespeare = "methinks it is like a weasel"
    new_sentence = generate(lenStr)
    
    best_score = 0
    new_score = score(shakespeare, new_sentence)
    best_sentence = ""
    num = 0
          
    while score(shakespeare, new_sentence) != 100:
        num += 1
        
        if new_score > best_score:
            best_score = new_score 
            best_sentence = new_sentence
            print(f"best score:{new_score} best sentence: {new_sentence}\n\n")
        
        # after every million executions, print the best score    
        if num%1000000 ==0:
            print(f"Result after {num} :")
            print(f"best score:{best_score} best sentence: {best_sentence}\n\n")
            
        new_sentence = generate(lenStr)
        new_score = score(shakespeare, new_sentence)
    

## timer to check the total time
start = timeit.default_timer()
if __name__ == '__main__':
     main()
stop = timeit.default_timer()
print('\n'+'Start Time: ' + '00.0' + ' sec' + '\nStop Time: ' + str(stop) + ' sec')


                
    
    
        
  

