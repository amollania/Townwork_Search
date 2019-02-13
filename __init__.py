from tkinter import *
from listcatch import *
from Search import *
from Tkintergui import *

window = Tk()
listbox = Listbox(window)

title = []
links = []

fileDir = os.path.dirname(os.path.abspath(__file__))
req = requests.get('https://townwork.net/tokyo')


def categoryget():
        req = requests.get('https://townwork.net/tokyo')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        soup = soup.body
        job = soup.find('li', id='jbTypeLmtForm')
        link_lists = job.find_all('li', class_='jsc-selection-group')

        p = re.compile('''<a[^>]+href=["'](.*?)["']''')

        for a in link_lists:
                link_results = a.find_all('a', href=True)
                for b in link_results:
                        link_link = p.findall(str(b))
                        title.append(b.text)
                        links.append(link_link[0])

        print("카테고리를 가져왔습니다.")

categoryget()

def access(url_home):
    req = requests.get('https://townwork.net/'+url_home)

def tkinter_gui():
    window.title("Clear!")
    window.geometry("")

    window_img = PhotoImage(file=fileDir+"\kanna.gif")
    imgLabel = Label(window, image=window_img)
    imgLabel.pack()

    textLabel = Label(window, text="会社持ってこい")
    textLabel.pack()

    btn = Button(window, width="100", height="3", text="START")
    btn.pack()

    btn2 = Button(window, width="100", height="3", text="종료하기")
    btn2.pack()

    i = 0
    lb = Listbox()
    while i < len(title)-1:
        i += 1
        lb.insert(i, title[i])
    lb.bind("<Double-Button-1>", OnDouble)
    lb.pack()


def OnDouble(self):
    selection = lb.curselection()
    print("selection:", selection)


tkinter_gui()
window.mainloop()


print(title[1])
print(links[1])

print("did")
