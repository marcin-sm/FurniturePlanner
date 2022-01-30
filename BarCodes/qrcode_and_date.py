from turtle import width
from blabel import LabelWriter

label_writer = LabelWriter("BarCodes/item_template.html", default_stylesheets=("BarCodes/style.css",))
records = [
    dict(sample_id="4859276283", sample_name="4859276283", plate_width="10", plate_height="12", border_top="0.5", border_bottom="0.1", border_left="0.1", border_right="0.1", space="4" ),
    dict(sample_id="s02", sample_name="Plyta 2",plate_width="20", plate_height="7", border_top="0.1", border_bottom="0.5", border_left="0.5", border_right="0.5", space="2" ),
    dict(sample_id="s02", sample_name="Plyta 2",plate_width="8", plate_height="13", border_top="0.5", border_bottom="0.5", border_left="0.1", border_right="0.1", space="5" ),
]

label_writer.write_labels(records, target="BarCodes/qrcode_and_date.pdf")
