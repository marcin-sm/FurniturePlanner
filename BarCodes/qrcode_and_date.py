from turtle import width
from blabel import LabelWriter

label_writer = LabelWriter("BarCodes/item_template.html", default_stylesheets=("BarCodes/style.css",))
records = [
    dict(sample_id="4628935901", sample_name="4 628 935901",plate_width="8", plate_height="11", border_top="0.5", border_bottom="0.5", border_left="0.1", border_right="0.1", space="4", onStock=True ),
    dict(sample_id="4859276283", sample_name="4 859 276283",plate_width="12", plate_height="10", border_top="0.1", border_bottom="0.1", border_left="0.5", border_right="0.1", space="4", onStock=False ),
    dict(sample_id="4783926189", sample_name="4 783 926189",plate_width="22", plate_height="11", border_top="0.1", border_bottom="0.5", border_left="0.5", border_right="0.5", space="1", onStock=True ),
    dict(sample_id="4734654324", sample_name="4 734 654324",plate_width="11", plate_height="11", border_top="0.5", border_bottom="0.1", border_left="0.5", border_right="0.1", space="3", onStock=False ),
]

label_writer.write_labels(records, target="BarCodes/qrcode_and_date.pdf")
