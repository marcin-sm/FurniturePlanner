from sre_constants import IN
from turtle import width
from blabel import LabelWriter

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





label_writer = LabelWriter("BarCodes/item_template.html", default_stylesheets=("BarCodes/style.css",))
records = [
    dict(sample_id="4628935901", sample_name="4 628 935901",Lwidth= "720", Lheight="510" ,plate_width=str(Prop(510,720,"W")), plate_height=str(Prop(510,720,"H")), border_top="0.7", border_bottom="0.7", border_left="0.1", border_right="0.1", space=str(Prop(510,720,"S")), onStock=True, number="1" ),
    dict(sample_id="4628935901", sample_name="4 628 935901",Lwidth= "730", Lheight="600" ,plate_width=str(Prop(600,730,"W")), plate_height=str(Prop(600,730,"H")), border_top="0.7", border_bottom="0.7", border_left="0.1", border_right="0.7", space=str(Prop(600,730,"S")), onStock=False, number="23" ),
    dict(sample_id="4628935901", sample_name="4 628 935901",Lwidth= "2070", Lheight="510" ,plate_width=str(Prop(710,2070,"W")), plate_height=str(Prop(710,2070,"H")), border_top="0.7", border_bottom="0.7", border_left="0.7", border_right="0.7", space=str(Prop(710,2070,"S")), onStock=True, number="9" ),
    dict(sample_id="4859276283", sample_name="4 859 276283",plate_width="12", plate_height="10", border_top="0.1", border_bottom="0.1", border_left="0.7", border_right="0.1", space="4", onStock=False ),
    dict(sample_id="4783926189", sample_name="4 783 926189",plate_width="22", plate_height="11", border_top="0.1", border_bottom="0.7", border_left="0.7", border_right="0.7", space="1", onStock=True ),
    dict(sample_id="4734654324", sample_name="4 734 654324",plate_width="11", plate_height="11", border_top="0.7", border_bottom="0.1", border_left="0.7", border_right="0.1", space="3", onStock=False ),
]

label_writer.write_labels(records, target="BarCodes/qrcode_and_date.pdf")
