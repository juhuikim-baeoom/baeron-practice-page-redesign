#!/usr/bin/env python3
"""mockup/practice-socialwork.html 에서 Artifact 발행용 조각을 만든다.

Artifact 는 <!doctype>/<html>/<head>/<body> 를 발행 시점에 직접 감싸므로,
그 껍데기를 벗긴 본문만 넘겨야 한다. 저장소의 목업이 원본이고,
이 스크립트의 출력은 파생물이다. 목업을 고친 뒤 다시 실행한다.

사용: python3 tools/make-artifact.py <출력경로>
"""
import io, re, sys

SRC = "mockup/practice-socialwork.html"

def main():
    if len(sys.argv) != 2:
        sys.exit("사용: python3 tools/make-artifact.py <출력경로>")
    html = io.open(SRC, encoding="utf-8").read()
    head = re.search(r"<head>(.*?)</head>", html, re.S)
    body = re.search(r"<body>(.*?)</body>", html, re.S)
    if not head or not body:
        sys.exit("head 또는 body 를 찾지 못했다: " + SRC)
    # charset·viewport 는 Artifact 가 직접 넣으므로 제외한다.
    inner = re.sub(r'\s*<meta[^>]*(charset|name="viewport")[^>]*>\s*', "\n", head.group(1))
    io.open(sys.argv[1], "w", encoding="utf-8").write(inner.strip() + "\n" + body.group(1).rstrip() + "\n")
    print("생성:", sys.argv[1])

if __name__ == "__main__":
    main()
