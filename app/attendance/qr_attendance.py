import qrcode

def generate_qr(student_id):

    qr = qrcode.make(
        f"student:{student_id}"
    )

    qr.save(f"qr_{student_id}.png")