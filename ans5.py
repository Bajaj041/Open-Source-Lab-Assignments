def lensort(strings):
    return sorted(strings, key=len)

words = ["apple", "banana", "fig", "cherry", "date"]
print(lensort(words))

def extsort(files):
    return sorted(files, key=lambda x: x.split('.')[-1])

filenames = ["report.docx", "image.png", "notes.txt", "archive.zip", "data.csv"]
print(extsort(filenames))