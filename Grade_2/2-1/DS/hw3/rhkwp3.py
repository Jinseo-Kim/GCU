import time

MAX_WORD = 100
MAX_MEAN = 200

class Node:
    def __init__(self):
        self.word    = ""
        self.meaning = ""
        self.intword = []
        self.num     = 0
        self.prev    = None
        self.next    = None

head  = None
tail  = None
total = 0

def chg_intword(src):
    return [ord(c.upper()) for c in src]

def create_node(word, mean):
    node         = Node()
    node.word    = word[:MAX_WORD - 1]
    node.meaning = mean[:MAX_MEAN - 1]
    node.intword = chg_intword(word)
    return node

def insert_sorted(node):
    global head, tail, total

    curr = head
    while curr is not None and node.intword > curr.intword:
        curr = curr.next

    if curr is None:
        if tail is None:
            head = tail = node
        else:
            node.prev  = tail
            tail.next  = node
            tail       = node
    else:
        node.next = curr
        node.prev = curr.prev

        if curr.prev is not None:
            curr.prev.next = node
        else:
            head = node

        curr.prev = node

    total += 1

def assign_numbers():
    idx_n = 1
    curr  = head
    while curr is not None:
        curr.num = idx_n
        idx_n   += 1
        curr     = curr.next

def search(word):
    iw   = chg_intword(word)
    curr = head
    while curr is not None:
        if iw == curr.intword:
            return curr
        if iw < curr.intword:
            return None
        curr = curr.next
    return None


# ── (2) 개선: 알파벳 첫 글자별 인덱스 테이블 ──────────────────────────────────

alpha_index = {}

def build_index():
    curr = head
    while curr is not None:
        key = curr.word[0].lower()
        if key not in alpha_index:
            alpha_index[key] = curr
        curr = curr.next

def search_improved(word):
    iw   = chg_intword(word)
    key  = word[0].lower()
    curr = alpha_index.get(key, head)
    while curr is not None:
        if iw == curr.intword:
            return curr
        if iw < curr.intword:
            return None
        curr = curr.next
    return None


# ── 메인 ───────────────────────────────────────────────────────────────────────

def main():
    fp = open("randdict_utf8.TXT", "r", encoding="utf-8")

    print("사전 로딩 중...")

    for line in fp:
        line = line.rstrip('\n')

        split = line.find(':')
        if split < 0:
            continue

        word = line[:split].rstrip()
        mean = line[split + 1:].lstrip()

        if not word:
            continue

        insert_sorted(create_node(word, mean))

    fp.close()

    assign_numbers()
    print(f"총 {total}개 단어 로딩 완료.\n")
    print("단어를 입력하세요 (종료: quit)")

    while True:
        word = input(">> ")

        if word == "quit" or word == "exit":
            break
        if not word:
            continue

        r = search(word)
        if r:
            print(f"({r.num}) {r.meaning}")
        else:
            print(f"'{word}'를 찾을 수 없습니다.")


def benchmark():
    global head, tail, total, alpha_index

    head = tail = None
    total = 0
    fp = open("randdict_utf8.TXT", "r", encoding="utf-8")
    for line in fp:
        line  = line.rstrip('\n')
        split = line.find(':')
        if split < 0:
            continue
        word = line[:split].rstrip()
        mean = line[split + 1:].lstrip()
        if not word:
            continue
        insert_sorted(create_node(word, mean))
    fp.close()
    assign_numbers()

    import random
    all_words = []
    curr = head
    while curr:
        all_words.append(curr.word)
        curr = curr.next
    sample = random.sample(all_words, 10000)

    t0 = time.time()
    for w in sample:
        search(w)
    t_base = time.time() - t0

    build_index()
    t0 = time.time()
    for w in sample:
        search_improved(w)
    t_impr = time.time() - t0

    print(f"기존 연결리스트 저장 구조에서 랜덤한 1만개 단어 검색 : {t_base:.3f}초")
    print(f"개선된 연결리스트 저장 구조에서 랜덤한 1만개의 단어 검색 : {t_impr:.3f}초")


## 메인
print("1. 기본 사전  2. 성능 비교")
mode = input("선택: ").strip()
if mode == "2":
    print("사전 로딩 중...")
    benchmark()
else:
    main()
