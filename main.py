# 나만의 프롬프트 관리 프로그램

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "제품의 특징을 살린 매력적인 썸네일 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트",
        "content": "당신은 전문 IT 컨설턴트입니다. 사용자의 질문에 전문적으로 답변해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

def show_menu():
    print()
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def add_prompt():
    print()
    print("=== 프롬프트 추가 ===")

    title = input("제목: ")
    content = input("내용: ")
    category = input("카테고리: ")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print()
    print("프롬프트가 추가되었습니다.")


def show_prompt_list():
    print()
    print("=== 프롬프트 목록 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f'{i}. [{prompt["category"]}] {prompt["title"]} {star}')

    print()
    print(f"총 {len(prompts)}개의 프롬프트")

def show_by_category():
    print()
    print("=== 카테고리별 조회 ===")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    for i, category in enumerate(categories, start=1):
        print(f"{i}) {category}")

    choice = input("선택: ")

    if not choice.isdigit():
        print("잘못된 입력입니다.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(categories):
        print("잘못된 번호입니다.")
        return

    selected_category = categories[choice - 1]

    results = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            results.append(prompt)

    print()
    print(f"[{selected_category}] 카테고리 프롬프트:")

    if len(results) == 0:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(results, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f'{i}. {prompt["title"]} {star}')

    print()
    print(f"총 {len(results)}개의 프롬프트")

def search_prompt():
    print()
    print("=== 프롬프트 검색 ===")

    keyword = input("검색어: ")

    results = []

    for prompt in prompts:
        if keyword.lower() in prompt["title"].lower() or keyword.lower() in prompt["content"].lower():
            results.append(prompt)

    print()
    print("검색 결과:")

    if len(results) == 0:
        print("검색 결과가 없습니다.")
        return

    for i, prompt in enumerate(results, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f'{i}. [{prompt["category"]}] {prompt["title"]} {star}')

    print()
    print(f"{len(results)}개의 프롬프트를 찾았습니다.")

def show_prompt_detail():
    print()
    print("=== 프롬프트 상세 보기 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    number = input("프롬프트 번호 입력: ")

    if not number.isdigit():
        print("잘못된 입력입니다.")
        return

    number = int(number)

    if number < 1 or number > len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[number - 1]

    favorite_mark = "⭐" if prompt["favorite"] else "아니오"

    print()
    print("--------------------------------")
    print(f'제목: {prompt["title"]}')
    print(f'카테고리: {prompt["category"]}')
    print(f"즐겨찾기: {favorite_mark}")
    print("--------------------------------")
    print("내용:")
    print(prompt["content"])
    print("--------------------------------")


def manage_favorite():
    print()
    print("=== 즐겨찾기 관리 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    number = input("프롬프트 번호 입력: ")

    if not number.isdigit():
        print("잘못된 입력입니다.")
        return

    number = int(number)

    if number < 1 or number > len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[number - 1]

    if prompt["favorite"]:
        prompt["favorite"] = False
        print(f'"{prompt["title"]}" 프롬프트를 즐겨찾기에서 해제했습니다.')
    else:
        prompt["favorite"] = True
        print(f'"{prompt["title"]}" 프롬프트를 즐겨찾기에 추가했습니다.')



while True:
    show_menu()

    choice = input("선택: ")

    if choice == "1":
        add_prompt()

    elif choice == "2":
        show_prompt_list()

    elif choice == "3":
        show_by_category()

    elif choice == "4":
        search_prompt()

    elif choice == "5":
        show_prompt_detail()

    elif choice == "6":
        manage_favorite()

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("아직 구현되지 않은 기능입니다.")