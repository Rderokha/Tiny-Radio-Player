import random
import vlc
import time

urls = [
    "https://27363.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27693.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27573.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24233.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://26573.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://26683.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27583.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://26483.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27413.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://26653.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27383.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24363.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://26593.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24493.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24153.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27393.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24373.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27423.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://26663.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27613.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://27433.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24223.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://21933.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24483.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24413.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24403.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://26523.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24443.live.streamtheworld.com:443/ROCK_AND_POPAAC.aac",
    "https://24403.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://27583.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://24413.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://24153.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://27573.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://24483.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://27613.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://26593.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://27693.live.streamtheworld.com:443/ROCK_AND_POP.mp3",
    "https://24443.live.streamtheworld.com:443/ROCK_AND_POP.mp3"
]
stream_url = random.choice(urls)

def play_radio_stream(url):
    player = vlc.MediaPlayer(url)
    player.play()
    time.sleep(1)

    print(f"Now playing from: {url}")

def main():
    play_radio_stream(stream_url)

if __name__ == "__main__":
    main()
