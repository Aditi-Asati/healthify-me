import time
from pygame import mixer

def play_music(stop_signal: str, song: str) -> None:
    """

    @params

    stop_signal (str) -> input entered in the terminal to stop the song
    song (str) -> name of the .mp3 song file located in the same directory as the .py file

    Plays `song` after desired time interval and stops the song when the `stop_signal` is entered in the terminal
    """
    #starting the mixer
    mixer.init()

    #loading the music
    mixer.music.load(song)

    print(f"Playing {song}...")
    #start playing the music
    mixer.music.play()

    #taking input from the user to enter the `stop_signal`
    while True:
        entry = input(f"Enter '{stop_signal}' to stop the song: ")
        if entry.lower() == stop_signal:
            #stopping the music
            mixer.music.stop()
            break


def file_writing(activity: str) -> None:
    """
    @params

    activity (str) -> denotes eye movement, physical exercise or drinking water
    time (object) -> its a time object

    logs the activity along with the time at which the activity was performed in log_timestamp_file.txt
    """
    with open("log_timestamp_file.txt", "a") as f:
        if activity == "water":
            print("\nlogging water timestamp into the file...")
            f.write(f"Drank water - {time.asctime(time.localtime())}\n")
        elif activity == "eye":
            print("\nLogging eyes movement timestamp into the file...")
            f.write(f"Eyes movement done - {time.asctime(time.localtime())}\n")
        elif activity == "exercise":
            print("\nLogging physical activity timestamp into the file...")
            f.write(f"Physical activity done  - {time.asctime(time.localtime())}\n")


if __name__ == "__main__":

    #initialising time
    init_eyes = time.time()
    init_water = time.time()
    init_exercise = time.time()

    #setting up the time intervals for eye movement, drinking water and physical exercise
    eyes_interval = 1200
    water_interval = 3600
    exercise_interval = 2400

    while(True):
        # for eyes movement
        if ((time.time() - init_eyes) >= eyes_interval):
            print("\nIts your eyes movement time!")
            play_music("eydone", "eye.mp3")
            init_eyes = time.time()
            file_writing("eye")
        
        #for drinking water
        if ((time.time() - init_water) >= water_interval):
            print("\nIts time to drink water!")
            play_music("drank", "water.mp3")
            init_water = time.time()
            file_writing("water")

        # for physical activity
        if ((time.time() - init_exercise) >= exercise_interval):
            print("\nLets do some physical exercise!")
            play_music("exdone", "exercise.mp3")
            init_exercise = time.time()
            file_writing("exercise")

        #program checks the above mentioned conditions after every 2 secs
        time.sleep(2)

        
