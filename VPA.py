import cv2
import tkinter as tk
import numpy as np
'''
def play_video():
    
    cap = cv2.VideoCapture('hand_video.mkv')
    delay = int(900 / 30)
    

    while True:
        
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame2")
            break
        img=frame.copy()

        instruction2 = "          Press ESC to quit "

        cv2.putText(img,
                    instruction2,
                    (10, 20),                 # text position
                    cv2.FONT_HERSHEY_COMPLEX, # font type
                    0.5,                      # font scale
                    (0, 0, 0),         # font color 
                    1,                        # line thickness
                    cv2.LINE_AA)             # optional line type for smoother text

        
        # Overlay text indicating which hand is being captured.
        
        cv2.imshow("Webcam", img)
        #########cv2.moveWindow("Webcam", int(w_f-w_f/4), int(h_f/3))
        #cv2.imshow("title", title)
        # Exit on pressing the Escape key.
        if cv2.waitKey(delay) & 0xFF == 27:
            break

    #filename = f"hand_{hand}.jpg"
    #cv2.imwrite(filename, flipped)
    cap.release()
    cv2.destroyAllWindows()
'''



def main():
    # We'll store the hand choice in this variable.
    # Since we’re assigning it inside callbacks, we’ll use `nonlocal` or make it mutable (like a list/dict).
    #CapHand = None
    # Create the main Tkinter window.
    root = tk.Tk()
    root.title("Video Player Application")
    root.geometry("600x400+450+200")
    
    # Label to instruct the user.
    instructions = (
    "Place your video file in the same folder as the application.\n"
    "\n"
    'Rename the video file to "hand_video".\n\n'
    "Press the 'Start' button to begin playback."
    )

    label = tk.Label(root, text=instructions, font=("Arial", 16))
    label.pack(pady=20)
    
    
    # Callback for the "Right" button.
    def start():
        #root.withdraw()  # Hide the Tkinter window.
        root.destroy()
        #play_video()
        print("I LOVE YOU")
        #root.deiconify() # Show the window again after capturing.
                                                                        
        
    
  
    # Create and pack the buttons.
    button_start = tk.Button(root, text="Start", command=start, width=20, height=2, font=("Arial", 14))
    button_start.pack(pady=10)
    
    
    root.mainloop()
    
if __name__ == "__main__":
    main()