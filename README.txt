Python installation directory: C:\Programs (Standalone)\Python34\python.exe

How to use pip:
Navigate to "c:\Programs (Standalone)\Python34\Scripts" and run "pip freeze" to ensure it's working.


Sample Code to Not Forget:
    if audioFile.tag.comments:
        print("Comment: " + audioFile.tag.comments[0].text)
    else:
        print("No comments")

        # audiofile = eyed3.load("C:/_TQP/Temp/Test/Dog-Dog.mp3")
        # print(audiofile.tag.artist)
        # print(audiofile.tag.album)
        # print(audiofile.tag.title)
        #
        # audiofile.tag.artist = u"Dog"
        # audiofile.tag.album = u"Dog"
        # audiofile.tag.title = u"Dog"
        #
        # print(audiofile.tag.artist)
        # print(audiofile.tag.album)
        # print(audiofile.tag.title)
        #
        # new_filename = "C:/_TQP/Temp/Test/{0} - {1}.mp3".format(audiofile.tag.artist, audiofile.tag.title)
        # print("new_filename: " + new_filename)
        # os.rename('C:/_TQP/Temp/Test/Dog-Dog.mp3', new_filename)