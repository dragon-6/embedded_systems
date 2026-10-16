# embedded_systems

Raspberry Pi 4 원격 개발 실습 (week02)

## 실행 방법

```bash
cd ~/projects/week02
python3 -m venv .venv
source .venv/bin/activate
python remote_check.py
python system_info.py
```

## 실행 결과

- `remote_check.py`: 호스트 이름, Linux, aarch64, 파일 경로, 가상환경 여부(True)를 출력합니다.
- `system_info.py`: 호스트, 운영체제, CPU, 현재 시간을 출력합니다.