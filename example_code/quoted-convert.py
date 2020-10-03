import quopri

encoded_text='''
<html>
  <head><META http-equiv=3D"Content-Type" content=3D"text/html;charset=3Deu=
c-kr">
 =20
      <title></title>
  </head>
  <BODY>
<DIV>=BE=C8=B3=E7=C7=CF=BC=BC=BF=E4 =C4=AB=C6=E4=C8=B8=BF=F8
=BF=A9=B7=AF=BA=D0!<BR>=BF=E4=C1=F2 =C4=DA=B7=CE=B3=AA =B6=A7=B9=AE=BF=A1 =
=B8=B9=C0=CC=C8=FB=B5=E5=BD=C3=C1=D2?</DIV>
<DIV>&nbsp;</DIV>
<DIV>=C0=DA=BF=B5=BE=F7=B5=B5 =C8=FB=B5=E9=B0=ED =C1=F7=C0=E5=C0=CE=C0=BA =
=C5=F0=C1=F7=C8=C4 40=B3=E2 =BC=BC=BF=F9=C0=BB =BB=FD=B0=A2=C7=CF=B8=E9
=BE=D5=C0=CC =B8=B7=B8=B7=C7=CF=B1=E2=B5=B5
=C7=CF=C1=D2<BR>=C0=CC=B7=B8=B0=D4 =BE=EE=B7=C6=B0=ED =C8=FB=B5=E7=BD=C3=B1=
=E2=BF=A1
=BE=C8=C1=A4=C0=FB=C0=CE =B1=E6=C0=CC =C0=D6=BE=EE=BC=AD
=BE=CB=B7=C1=B5=E5=B8=AE=B0=ED=C0=DA =C7=D5=B4=CF=B4=D9.</DIV>
<DIV>&nbsp;</DIV>
<DIV>=C4=AB=C0=CC=B7=CE=C7=C1=B7=A2=C6=BD Doctor : =C4=A1=BF=AD=C7=D1
=B1=B9=B3=BB =C0=C7=B7=E1=BD=C3=C0=E5=BF=A1=BC=AD =BC=BA=B0=F8=C7=CF=B4=C2
=C1=F6=B8=A7=B1=E6=B7=CE =B1=DE=BA=CE=BB=F3! <BR>Doctor of Chiropratics
=C7=D0=C0=A7=C3=EB=B5=E6 =C0=CE=C1=F5=C0=C7 =C3=B6=B9=AE=C0=CC
=C8=B0=C2=A6 =BF=AD=B7=C1 =C0=D6=B4=E4=B4=CF=B4=D9.</DIV>
<DIV>&nbsp;</DIV>
<DIV>=C0=C7=BB=E7 =C7=D1=C0=C7=BB=E7, =B9=B0=B8=AE=C4=A1=B7=E1=BB=E7,
=BF=EE=B5=BF=BF=E4=B9=FD=BB=E7, =C3=DF=B3=AA =B8=C0=BB=E7=C1=F6
=C0=FC=B9=AE=B0=A1=BF=A1=B0=D4 =C8=F1=BC=D2=BD=C4=C0=CC=C1=D2<BR>=C0=CC=C1=
=A8
=B1=B9=B3=BB=BF=A1=BC=AD=B5=B5 =B9=CC=B1=B9=C0=CE=C1=F5 =C7=D0=C0=A7=C1=F5=
=BC=AD=B8=A6
=C3=EB=B5=E6=C7=D2 =BC=F6
=C0=D6=B1=B8=BF=E4<BR>=C0=CF=B9=DD =C7=D0=BB=FD=B5=B5
=B0=A1=B4=C9=C7=CF=B0=ED =C1=F7=C0=E5=C0=CE.=BB=E7=C8=B8=C0=CE=B5=B5
=B0=A1=B4=C9=C7=CF=B4=E4=B4=CF=B4=D9.</DIV>
<DIV>&nbsp;</DIV>
<DIV>=C0=DA=BC=BC=C7=D1 =BB=E7=C7=D7=C0=BA =BE=C6=B7=A1=B8=A6 =C2=FC=B0=ED=
=C7=CF=BC=BC=BF=E4</DIV>
<DIV>&nbsp;</DIV>
<DIV><A href=3D"https://soo.gd/ZWIu">https://soo.gd/ZWIu</A></DIV>
<DIV><BR>&nbsp;</DIV>
  </BODY>
</html>'''

decoded_text=quopri.decodestring(encoded_text).decode('ansi')

print(decoded_text)

'''
output

<html>
  <head><META http-equiv="Content-Type" content="text/html;charset=euc-kr">
  
      <title></title>
  </head>
  <BODY>
<DIV>안녕하세요 카페회원
여러분!<BR>요즘 코로나 때문에 많이힘드시죠?</DIV>
<DIV>&nbsp;</DIV>
<DIV>자영업도 힘들고 직장인은 퇴직후 40년 세월을 생각하면
앞이 막막하기도
하죠<BR>이렇게 어렵고 힘든시기에
안정적인 길이 있어서
알려드리고자 합니다.</DIV>
<DIV>&nbsp;</DIV>
<DIV>카이로프랙틱 Doctor : 치열한
국내 의료시장에서 성공하는
지름길로 급부상! <BR>Doctor of Chiropratics
학위취득 인증의 철문이
활짝 열려 있답니다.</DIV>
<DIV>&nbsp;</DIV>
<DIV>의사 한의사, 물리치료사,
운동요법사, 추나 맛사지
전문가에게 희소식이죠<BR>이젠
국내에서도 미국인증 학위증서를
취득할 수
있구요<BR>일반 학생도
가능하고 직장인.사회인도
가능하답니다.</DIV>
<DIV>&nbsp;</DIV>
<DIV>자세한 사항은 아래를 참고하세요</DIV>
<DIV>&nbsp;</DIV>
<DIV><A href="https://soo.gd/ZWIu">https://soo.gd/ZWIu</A></DIV>
<DIV><BR>&nbsp;</DIV>
  </BODY>
</html>

'''