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

print("프롬프트 기본 데이터가 등록되었습니다.")
print("등록된 프롬프트 수:", len(prompts))