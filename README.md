# AIDLE

## code
자유롭게 얘기하고 자유롭게 수정가능
<br><br>**파싱을 위한 코드 파일**
<br>실행 순서
<br>parsing(using_eml-parser) -> split_date_from_src -> find_origin_sender
<br>각 단계에서 나온 결과 csv를 다음단계 시작전에 읽어 사용

- parsing(using_eml-parser) 
<br> eml 파일들을 읽어 eml-parser를 이용해 각 파일의 헤더부분 파싱해서 각각 해당 열에 추가, html 부분 전체 파싱해서 'html' 열에 추가
- split_date_from_src
<br> /header/received/0/src 부분에서 at 뒤의 시간 정보 부분 파싱하여 /header/received/0/src_at에 저장
<br> 하는 이유: /header/received/0/date에 제대로 저장안된 듯 보여서
<br> cf. /header/received/0/src 내용은 헤더에서 가장 마지막에 쌓인 received 정보
- find_origin_sender
<br> 각 헤더에 쌓인 received 중 가장 아래의 부분(최초로 발송될 때의 발신자, 수신자 정보)을 각 행의 ori_sender_ip, ori_sender_server, ori_receiver_mail에 저장
<br> 하는 이유: 최초 발신자, 수신자 정보를 분석에 사용하기 위해

**html 부분(메일 본문 부분) 디코딩(처리)을 위한 코드 파일**
- mailbody_decoder
<br> <'html>태그만 뽑혀있는 'csv'파일에 대해서만 현재 처리 가능
<br> '=' 문자가 포함되어 있는 경우 디코딩이 안되기 때문에 '='을 없애고 빈칸으로 치환
<br> html 태그 내의 '='을 전부 ' '로 치환할 경우 내용이 일그러지기 때문에 <'div>태그에 대해서만 적용
<br> 요기까지 했음 -> 완료되면 업데이트

## EDA
각자 나름의 방법으로 분석한 내용 공유
