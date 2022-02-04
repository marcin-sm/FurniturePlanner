#from sre_constants import IN
#from turtle import width
from blabel import LabelWriter
#from numpy import sign


def Prop (width,height,ret):
    Xmax = 23.5
    Ymax = 15
    INwidth = 0
    INheight = 0
    OUTwidth = 0
    OUTheight = 0
    
    if width > height:
        INwidth = width
        INheight = height
    else:
        INwidth = height
        INheight = width

    ratio = INwidth/INheight

    if Xmax / ratio > Ymax:
        OUTwidth = ratio*Ymax
        OUTheight = Ymax

    else:
        OUTwidth = Xmax
        OUTheight = Xmax/ratio

    if ret == "W":
        return OUTwidth

    elif ret == "H":
        return OUTheight

    elif ret == "S":
        return (52.5 -16.9- 12 - OUTwidth)/3

    elif ret == "w":
        return INwidth

    elif ret == "h":
        return INheight 

def CreateEntry (width, height, edgesTaped:list, code, info, sign, onStock):

    borders = ["0.7" if True else "0.1" for x in edgesTaped]
    return (dict(sample_id=info, sample_name=code,Lwidth= str(Prop(width,height,"w")), Lheight=str(Prop(width,height,"h")) ,plate_width=str(Prop(width,height,"W")), plate_height=str(Prop(width,height,"H")), border_top=borders[0], border_bottom=borders[2], border_left=borders[1], border_right=borders[3], space=str(Prop(width,height,"S")), onStock=onStock, sign=sign ))



label_writer = LabelWriter("Labels/operation_template.html", default_stylesheets=("Labels/style.css",))
records = [
    dict(sample_id="http://192.168.100.12:8001/?code=CUT", sample_name="CIĘCIE", OimgPath = "Labels/Operations/CUT.png", space = "3"),
    dict(sample_id="http://192.168.100.12:8001/?code=TAPE", sample_name="OKLEJANIE", OimgPath = "Labels/Operations/TAPE.jpg",space = "3"),
    dict(sample_id="http://192.168.100.12:8001/?code=DRILL", sample_name="WIERCENIE", OimgPath = "Labels/Operations/DRILL.png", space="3"),
    dict(sample_id="http://192.168.100.12:8001/?code=PAINT", sample_name="MALOWANIE", OimgPath = "Labels/Operations/PAINT.png"),
    dict(sample_id="http://192.168.100.12:8001/?code=STORE", sample_name="MAGAZYN", OimgPath = "Labels/Operations/STORE.jpg"),
    dict(sample_id="http://192.168.100.12:8001/?code=PACK", sample_name="PAKOWANIE", OimgPath = "Labels/Operations/PACK.png"),
    dict(sample_id="http://192.168.100.12:8001/?code=PREVIEW", sample_name="INFO", OimgPath = "Labels/Modes/PREVIEW.png"),
    dict(sample_id="http://192.168.100.12:8001/?code=REPORT", sample_name="RAPORT", OimgPath = "Labels/Modes/REPORT.png"),
    dict(sample_id="http://192.168.100.12:8001/?code=WORKER1", sample_name="JAN", OimgPath = "Labels/Modes/WORKER.png"),
    dict(sample_id="http://192.168.100.12:8001/?code=WORKER2", sample_name="KAROL", OimgPath = "Labels/Modes/WORKER.png"),
    dict(sample_id="http://192.168.100.12:8001/?code=WORKER3", sample_name="ADAM", OimgPath = "Labels/Modes/WORKER.png")
]

label_writer.write_labels(records, target="Labels/OperationsModes.pdf", base_url=".")
