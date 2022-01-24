from abc import ABC, abstractmethod

class MediaPlayer():
    def __init__(self, player):
        self.__player = player

    def execute(self):
        self.__player.play()

    class Target(ABC):
        @abstractmethod
        def play(self):
          raise NotImplementedError

    class AudioPlayer(Target):
        def play(self):
            print("Play audio")

    class VideoPlayer(Target):
      def play(self):
        print("Play videoMP4")

    class VideoAdapter(Target):
        def __init__(self, externalPlayer):
          self.__external_Player = externalPlayer = externalPlayer

        def play(self):
          self.__externalPlayer.play_mp4()

