#This function tries to bring a bit of transition effect on program_start_up
#//works as expected but may need some proper way of doing it
import thread,time
#window.attributes('-transparentcolor','green2') #This will make spacified color transparent in the window            
def transition_thread(threadName,delay,window):
            global visible;
            visible = 0.0;
            while(visible < 1.1):
                visible = visible +0.1;
                time.sleep(0.1);
                window.attributes('-alpha',visible);
