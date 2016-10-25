name = raw_input ('Welcome! What is your name?: ')


if name == 'aidan'or name == 'Aidan': 
        
        
        while True:             
            password = raw_input ('Please enter your password: ')
            
            if password == '12345a':
                print 'Welcome back Aidan!'
                break
            else:
                print 'Access denied. Please try again'
            
  
else:
    print 'Access denied. The police have been notified and will arrive in 2 minutes'
