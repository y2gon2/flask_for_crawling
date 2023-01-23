import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(email, corp_name):
    # 세션설정
    s = smtplib.SMTP("smtp.gmail.com", 587)

    # TLS 보안시작
    s.starttls()

    # 로그인 인증
    s.login("y2gon2@gmail.com", "sgaadtpxjnzkpndm")

    # 보낼 메세지 설정
    msg = MIMEMultipart()
    msg["Subject"] = "주식 종목 (%s) 크로링 결과 자료 송부합니다." % corp_name
    msg["From"] = "y2gon2@gmail.com"
    msg["To"] = email

    msg.attach(MIMEText(corp_name, " : 유첨파일 참조"))
    file_path = "data\\%s.txt" % corp_name
    file = open(file_path, "rb")
    part = MIMEApplication(
        file.read(),
        Name=basename(file_path)
    )
    # after the file is closed
    part["Content-Disposition"] = 'attachment; filename="%s"' % basename(file_path)
    msg.attach(part)

    # 메일보내기
    s.sendmail("y2gon2@gmail.com", email, msg.as_string())

    # 세션 종료
    s.quit()

