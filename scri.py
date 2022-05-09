import os
import shutil
path = "/Poesia escenica vi - circ, magia i titelles/"
pathend = path + "complet/"
i = 1
cote = "pages de droite impaires/"
newdir = "." + path + "complet"
if not os.path.exists(newdir):
    os.makedirs(newdir)
for file in sorted(os.listdir("." + path + cote)):
    if str(file)[-5] in ["a", "b", "c", "d", "e", "f", "g"]:
        i = i - 2
        newname = str(i) + str(file)[-5] + ".jpg"
    else:
        newname = str(i) + ".jpg"
    cwd = os.getcwd()
    shutil.copy2(cwd + path + cote + file, cwd + pathend + newname)
#    cwd = os.getcwd()
#    os.rename(cwd + path + "pages de droite impaires/" + file, cwd + path + "pages de droite impaires/" + newname)
    i += 2
    print(file, newname)

exec(open("scri2.py").read())
