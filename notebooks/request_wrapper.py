import requests
import time

def request_wrapper(req,max_retries,*arg1):
    counter = 0
    while counter < max_retries:
        try:
            response = req(*arg1)
            return response
            break
            
        except requests.ConnectionError:
            counter += 1
            if counter == max_retries:
                print 'Connection Error encountered '+str(max_retries)+' times' 
                time.sleep(0.2*counter)
            
        except requests.Timeout:
            counter += 1
            if counter == max_retries:
                print 'Timed Out '+str(max_retries)+' times' 
                time.sleep(0.2*counter)