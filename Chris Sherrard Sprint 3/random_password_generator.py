import random
import string
class Generator:
   
    def Random_password():
        final_password = ""
        password_length = 0
        password_n = []
        password_a = []
        password_p = []
        password_a = string.ascii_letters
        password_n = string.digits 
        password_p = string.punctuation 
        ts_final_password = []
        while password_length < 12:
                  
              ts_final_password.append (password_a[random.randint(0, len(password_a)-1)])
              ts_final_password.append(password_p[random.randint(0, len(password_p)-1)])
              ts_final_password.append(password_n[random.randint(0, len(password_n)-1)])
        
             
              password_length += 1        
              
        password_length = 0
        i=0
        while password_length < 12:
            
            final_password +=  ts_final_password[random.randint(0, len(ts_final_password)-1)]   
           
            password_length += 1        
        while i<11:
            if final_password[i] == final_password[i+1]:
                final_password[i+1] = "}"
            i+=1    
        return(final_password)
user_input = input("""For what platform is the password?
> """)

print(f"""The following is your {user_input} password:
"""+ Generator.Random_password())
     