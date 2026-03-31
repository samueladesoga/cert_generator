# utils.py
import fitz  # PyMuPDF


def create_certificate_for(name: str) -> str:
    doc = fitz.open("SDN_2026_cert.pdf")
    page = doc[0]

    # Register the custom font so it is embedded in the output PDF
    page.insert_font(fontname="amsterdam", fontfile="Amsterdam.ttf")
    font = fitz.Font(fontfile="Amsterdam.ttf")

    fontsize = 60
    text_color = (0, 0, 0)  # black

    # The PDF has Rotation=90, so the underlying coordinate space is portrait
    # (595 wide × 842 tall) while the display is landscape (842 wide × 595 tall).
    # insert_text works in underlying space, so we must:
    #   1. Map display (landscape) coordinates to underlying (portrait) coordinates.
    #   2. Pass rotate=90 so the text baseline runs in the landscape x-direction.
    #
    # Mapping for Rotation=90:
    #   underlying_x = display_y
    #   underlying_y = 842 - display_x_start   (text advances upward = –y in underlying)
    text_length = font.text_length(name, fontsize)
    display_y = 300                              # vertical position — adjust if needed
    display_x_start = (842 - text_length) / 2   # centre horizontally in landscape view

    underlying_x = display_y
    underlying_y = 842 - display_x_start

    page.insert_text(
        (underlying_x, underlying_y),
        name,
        fontname="amsterdam",
        fontsize=fontsize,
        color=text_color,
        rotate=90,
    )

    file_name = "generated/" + name + ".pdf"
    doc.save(file_name)
    doc.close()
    return file_name