# ELK

# Run
```sh
# 실행
$ docker-compose up -d

# 도커 접속
$ docker exec -it elasticsearch bash

# 키바나 토큰 값 획득
$ bin/elasticsearch-create-enrollment-token --scope kibana

# 패스워드 설정
$ bin/elasticsearch-setup-passwords interactive

# 키바나 접속 후 토큰 값 붙여넣기
# 키바나 도커 로그에서 6자리 핀번호 입력
# 설정한 패스워드로 elastic/pw 로그인


```