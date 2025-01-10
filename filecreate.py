import shelve

def main():
    d = shelve.open('score.txt')  # here you will save the score variable   
    d['score'] = 0            # thats all, now it is saved on disk.
    d.close()   

main()