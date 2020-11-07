from pytube import YouTube, Playlist
from pyfiglet import Figlet
import os

from pytube.exceptions import RegexMatchError


def baixarVideo(url):
    try:
        video = YouTube(url)
        print("[ {} ]".format(video.title.upper()))
        print("Download começando")
        video.streams.get_highest_resolution().download()
        print("Download completo")
    except RegexMatchError:
        print('Link invalido')


def baixarPlaylist(url):
    try:
        playlist = Playlist(url)
        print("[ {} ]".format(playlist.title.upper()))
        print("Download começando")
        playlist.streams.get_highest_resolution().download()
        print("Download completo")
    except RegexMatchError:
        print('Link invalido')


def seleciona():
    print("[1] Baixar vídeo (MP4)\n[2] Baixar Playlis (MP4)\n[3] Sair")
    escolha = int(input("> "))

    if escolha == 3:
        return False
    else:
        print("")
        URL = str(input("URL: "))

        print("")
        if escolha == 1:
            baixarVideo(URL)
        elif escolha == 2:
            baixarPlaylist(URL)
        else:
            print("Comando invalido")
    return True


def main():
    loop = True
    custom_fig = Figlet(font='small')
    while loop:
        print(custom_fig.renderText('PyTube'))
        loop = seleciona()
        if loop:
            print("\n")
            os.system("pause") or None
            os.system('cls') or None


if __name__ == '__main__':
    main()
