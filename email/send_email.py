import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from dotenv import load_dotenv

load_dotenv()

# Email credentials
sender_email = os.environ.get("SENDER_EMAIL")
password = os.environ.get("SENDER_PASSWORD")
receiver_email = os.environ.get("RECEIVER_EMAIL")

print(f"Sender: {sender_email}")
print(f"Receiver: {receiver_email}")

# Read email template
template_path = os.path.join(os.path.dirname(__file__), 'email-template.html')
with open(template_path, 'r', encoding='utf-8') as f:
    html_template = f.read()

# Replace image URLs with embedded references
html_template = html_template.replace(
    'id="m_-8007825961398364423image_0" src="https://ci3.googleusercontent.com/mail-img-att/AGAZnRqH-0ghQaDwZ5rshlSmdUPwGWz2MJs3VSLyipbVsQD1TjREdh9ZKiO2Nup-37-ynTNu_VsnMxj-ALmdZzHmuKsws-vWRUHFOaJ-wlFD3woLU0h_giZaeSJiL3hLjKubOubDfqCt3flG1lj8Ms7DDjGvE6AHfFK9_po4bIfMt7qSvoupbOaoPwyxhRq6aDJJ0BrTSk241InL5VFzgiS89AbY-eP-aDddW97i1CZasfUpWq3RjADVOWg_Sp7L_gUG4oi9tOJptlyagQMqoHD4EXJZ4pvPZ7gWiXtR94s1P_HaQmaSRUspXTR8ZE3vV9OucpdRkspwtk4wdfLTLT8a_-YXuWgH-nz0nZEipXKzyhKFT_pB-xLE7F0eFpPGjEc03hDnCehmptOLCfQ-S0_U5x952KWtsyy4nC-NobPmN8e49wbZ5CuWpCsWyVjEv-Gp8NXhbPmMDGsMEip6iaAcX_iufKDf5p825IGbl6xcvxptQhAt1xywDc4c433q91zBcP_EKmY3QYEczQ4xW4uhYnet9tqH9C0MoTEGwocfgAHixEsgp0Gd00IYpvOFYnvUZR9O0o6Xe756bjOpe4LJFR7Jgk21ajwa4oRwvZ7VTJPT6u8Vt92MPmyrsD-ddAaSyn8kFIdlb1-cf1_VHMklA_OOn0v3QlyaNlkiKXHnv5xu5v27qndGDD0UPr07gq2snk3B3Q9keMjUMgamUHhyEyI14oaQEq6QgLrksmSqj-q5edrQuWi14dpTmJexpBLDjDsyG8Kv-MRCTg5xfbzLUncC08M-FqUuc5sib_8rWJh5TopP1QCLiue05J_QUC-buTwtYYuBjKTRTNL0hiA4zRoh_iDfyHOA2fYZwEADWLWYwK7rC34a3Hgk6mXOhZOUsHR9StvylTnK9U_bP_Od9qwkjiVN0CEpf-6kejPsswwnmJRCRjyFA7EKqw_LB4U4pwRujJJZZq8dfATShAoRbeODqiX4f2EUYg0Tm77tR56TcsQrtHRAw957jfjbqFjgdFpofzombXyc7FAtReQE1J0tq684eU-pdCZKh3oe5rMFP0MEuj4ZABOwEFPXz0b4ay-Yxjp8RgMcYttIpG38p4y3ooP8EAuy59kGRA1pQndUY8g74A0azzC1rnENIupVpc0vk5NSrsl0c1rjMwreKrod2FCFa2dOBCZ2HRihMUu-pbl6koxJlVC_o20=s0-l75-ft"',
    'src="cid:image001"'
)
html_template = html_template.replace(
    'id="m_-8007825961398364423image_2" src="https://ci3.googleusercontent.com/mail-img-att/AGAZnRrWN94BcOqHvv4yVE28ZJ7Ka-cqeiZmNMDIbhR0rlybZuNQ5tCNHv9KuGFRGYWFGGLr-JOKj1uqBwTaIP6uCXWtK95OPo1xuZnD7FaFi1zRRWSjuHBqNf2ixM5P0EZVxgGm-iPb59pP3kp_tnbg3kAy6i2vsiRFMAgqoUVGp3_a1U5dfwbaOlzzSPvcWzHjb7mz0lkUB1Mq-EPpYjUX0Urj_p7BZa1OBAyEppx4B1Pg79wXq1TVq71FvxN7pgZJkulDuDAXzNZwnelTtK54S-EiefR633VtQDypmi52I-ieLFQj-vX-XDtu7b-5Q7OwBndtcbMxNOHeZ-OMcdvTp4GuQAqUsPH7pskGNJ1VTd_M4o5D9XQJPCnO1jzD5ifmW3HEgnGFtFUenm1r7urDOqJXFPXtsT88pcBiQAJLFQeOQoUb0yhsKRfG91AEVME2Z1KpVvVGVSCctTFXFzjM1PRZZ5VBW3okNcBQTkukxVLZh6mObhCtEXt3vwwEqQwmZN38iFzI3nn8aODndcsh9Hq_iQhTtkhBEfSDFao7nc0uzZkZEgYmU1MhE_DigeKZnMJOqLOOTkmRo6Zq-Mb9C4b7U5CH90Apms47kHXwhFUpbzrW_kKqid64oGCB3VoBicE5BkCpm-ADYE9Q5KdOvLv9ShGZ-6mTUhsQW8l_qv-UAoslao8PS_1r7Qka3--1xGU6bFfN4jd8F_CWFfGMuyWp4QdRgjSxuzs5x--H1qujjO1V6YZ7AaB38p7I9NDo8Bi_qhzQ6bCinAqVwBnJYPfvijiEBzxdOl2QkyaGRMPGeVz6ZLQ-XuEi3h0q7qLieG8WQ0s69JBYzCvVZCDKaWsdqGtmX8PpxiR_g3ylJReWmrwuLzwvV36r6we6bcFKvFUb9CMQyIeJ4X2Qirip4ewL701TuLmPSpcIxsUOYv6HyEj2re2D35AGq4eKzYujS4plegVpbJe4JuW-92YIOyhX1qECsiFS-Ag2kytXBSPsQ0moIPaIsuFx7QFb-fZ32e39fk-qQWzh0t6SxGzWli2KZZU_njzuLeql6UTgTZ3b2IQioub_jtl03vt60l4d99Hh1xCZtwciJLfZM6HMiiLip_XIZ8bI224ruk-MYr0vvwghSnM_ZQ8wlwjf844pYKJrvjpr-7pwDg10sDXpy_KzAYBOAPGrRZcnzeZn96-S1ipIOsYayHKRMAvv=s0-l75-ft"',
    'src="cid:image002"'
)
html_template = html_template.replace(
    'id="m_-8007825961398364423image_1" src="https://ci3.googleusercontent.com/mail-img-att/AGAZnRrME4jDuvZTJrnuVZgfPfKoyvSy4PQegEJTVQGz-mCUisLPgVnpI_tFcEm6ibrkPDfYN5bAXGAT-4KHivx9N8XWAWgu7Ohdz_lNCx57Dr60dZCiL0tvossbM3xueu_jILHuYS_gRdAhoRptg_eeUIJGzJZYQyPpB6UtDsLmLfKqrHeClN4dcLlZ3IXF-cnqU8UdoVy8MHhMVT2OUjXT0ULggq67tfd7YpUNbQ--g1SyaynxgSmQTgjK0zgSbBfpVTyGobMRZiEFfFYv5z1CTUV3ZrDjkDB4wm36NMYq44z6eHdo0_bcHy_qfX8aZBlPhnoa8K-Kb7u5FOIeombTqRi1ILxcIDBzvr6ObTlsqnewGDO3xyvlpXSmS63Q9A9C4rwGpL27NSErBRNtcjQGhdG_Z3ru08sSdjCpouFPwemRUvDrEk0_r_6wA9hli8rj_eZIHy-g5eEgQvbgrXtgF8yCzJfG5SmpH6rNU5HYT7C-1pXm7uVEtcp6QJ_85sKLdsZbBYZwJw7Qa4ut32s14fgzxJg1H9Uy9h88bIPm3gYlAbTGek9eMP9V9rg_Uw44mHeg1HRryXOJTaFw7s_ggSdmjGaODEIJwDRGQh6L1HbZ_8MawChXfHReNgxJj-mqksQvOJc6OR4KM-SGHzkIaVNXvn0wzILhltVNSZlb4sks6DPMBuTSZZkYkPy_Ux4A0Zh3WyB3YC0eMB38fc8n1gueX8ZC5xk4WnSgi62flKxeTPN8n5rekZRuyyvf1cHeJ_QLA5pk0fCMtXPqs_SqqrXWPxP0pJILuOo7HPGLunTMddzIBC767KZhhz0339uRzBvsGsToiFwumr8_d9X3GxjSpsMQZ506ZsbAoK0YagNakIG3Hl-Qvo6MhlM_8xNlOhVCsDbrhja3p77C72q6pIq-cBqmBEMZovMxC58OUaYgY30oBayWVVp8FgP2CiDdqyskxQmD7t6t4_o44Ht3GvUwB_sMb1pOGG1GQHc-YGUb4JrpIErmj-aJ2YxcNJkfrvv_wJDQZkXdh-BwV5vMRuztju8MTQ0MrVBae4lA3urkdQn8X9lC6tdeemcLbwx1wwRo0c6twah2PHaEQ4jNs8XxCJBg-oT9Z6Jmmvc2xzkVlG6SpHv7yCnWIb5YjdDbs412hjutIjZkqcj28ScqCaBwYOiuCNT79ujWS6aiwuVNREem5bateME0_6w2ag=s0-l75-ft"',
    'src="cid:image003"'
)

# Create message
msg = MIMEMultipart("related")
msg_alternative = MIMEMultipart("alternative")
msg.attach(msg_alternative)

msg["Subject"] = "DATIC Informa: Sobre el Incidente de Bloqueo de Cuentas"
msg["From"] = "DATIC Informa"
msg["To"] = receiver_email

# Attach HTML template
msg_alternative.attach(MIMEText(html_template, "html"))

# Attach images
image_files = {
    'image001': 'image001.png',
    'image002': 'image002.png',
    'image003': 'image3.png'
}

for image_id, filename in image_files.items():
    image_path = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(image_path):
        with open(image_path, 'rb') as attachment:
            image = MIMEImage(attachment.read())
            image.add_header('Content-ID', f'<{image_id}>')
            image.add_header('Content-Disposition', 'inline', filename=filename)
            msg.attach(image)
        print(f"✓ Attached {filename}")
    else:
        print(f"✗ Warning: {filename} not found")

# Send email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("✓ Email sent successfully!")
except Exception as e:
    print(f"✗ Error sending email: {e}")