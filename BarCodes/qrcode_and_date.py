from blabel import LabelWriter

label_writer = LabelWriter("BarCodes/item_template.html", default_stylesheets=("BarCodes/style.css",))
records = [
    dict(sample_id="s01", sample_name="Plyta 1"),
    dict(sample_id="s02", sample_name="Plyta 2"),
]

label_writer.write_labels(records, target="BarCodes/qrcode_and_date.pdf")
