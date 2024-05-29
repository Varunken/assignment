def file_editor(path,text):
    try:
      data = open(path)

      try:
        data.write(text)

      except:
        print("Unable to write the data. Please add an append: 'a' or write: 'w' parameter to the open() function.")

      finally:
        data.close()

    except:
      print(f"{path} file is not found!!")