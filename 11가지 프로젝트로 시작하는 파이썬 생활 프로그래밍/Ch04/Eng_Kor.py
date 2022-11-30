# -*- coding: utf-8 -*-
## 영어
import re,usecsv,os
K = """
알츠하이머병에서 뇌의 파괴를 늦추는 최초의 약물이 중대한 것으로 예고되었습니다.

이 연구의 돌파구는 수십 년간의 실패를 끝내고 치매의 가장 흔한 형태인 알츠하이머를 치료하는 약물의 새로운 시대가 가능함을 보여줍니다.

그러나 레카네맙이라는 약은 효과가 미미하고 사람들의 일상생활에 미치는 영향에 대해서는 논란이 있습니다.

그리고 그 약은 질병의 초기 단계에서 작용하기 때문에 대부분은 그것을 발견하는 혁명 없이는 놓칠 것입니다.

Lecanemab은 알츠하이머 환자의 뇌에 축적되는 베타 아밀로이드라고 하는 끈적끈적한 총구를 공격합니다.

실패, 절망, 실망으로 점철된 의료계에 일부에서는 이러한 시험 결과를 승리의 전환점으로 보고 있습니다.

영국 알츠하이머 연구소는 이번 발견이 "중요하다"고 말했다.

30년 전 아밀로이드를 표적으로 삼는 아이디어를 고안한 세계 최고의 연구자 중 한 명인 John Hardy 교수는 이것이 "역사적"이며 "우리는 알츠하이머 치료법의 시작을 보고 있다"고 낙관했습니다. 에든버러 대학교의 Tara Spires-Jones 교수는 "오랫동안 실패율이 100%였기 때문에 결과는 큰 문제"라고 말했습니다.

치매: 위험을 낮출 수 있는 라이프스타일 변화
노인 슈퍼 브레인의 수수께끼에 대한 신선한 단서
'그렇게 - 내가 사랑하는 여자가 변했다'
젊은 알츠하이머 환자 지원 요청
현재 알츠하이머병 환자에게는 증상을 관리하는 데 도움이 되는 다른 약물이 제공되지만 질병의 진행 과정을 변화시키는 것은 없습니다.

레카네맙은 신체가 바이러스나 박테리아를 공격하기 위해 만드는 것과 같은 항체로, 뇌에서 아밀로이드를 제거하도록 면역 체계에 지시하도록 조작되었습니다.

아밀로이드는 뇌의 뉴런 사이 공간에서 서로 뭉쳐 알츠하이머 병의 특징 중 하나인 독특한 플라크를 형성하는 단백질입니다.
"""

E = """
The first drug to slow the destruction of the brain in Alzheimer's has been heralded as momentous.

The research breakthrough ends decades of failure and shows a new era of drugs to treat Alzheimer's - the most common form of dementia - is possible.

Yet the medicine, lecanemab, has only a small effect and its impact on people's daily lives is debated.

And the drug works in the early stages of the disease, so most would miss out without a revolution in spotting it.

Lecanemab attacks the sticky gunge - called beta amyloid - that builds up in the brains of people with Alzheimer's.

For a medical field littered with duds, despair and disappointment, some see these trial results as a triumphant turning point.

Alzheimer's Research UK said the findings were "momentous".

One of the world's leading researchers behind the whole idea of targeting amyloid 30 years ago, Prof John Hardy, said it was "historic" and was optimistic "we're seeing the beginning of Alzheimer's therapies". Prof Tara Spires-Jones, from the University of Edinburgh, said the results were "a big deal because we've had a 100% failure rate for a long time".

Dementia: Lifestyle changes that could lower your risk
Fresh clue to mystery of elderly super brains
'Just like that - the woman I love changed'
Calls for support for young Alzheimer's sufferers
Currently, people with Alzheimer's are given other drugs to help manage their symptoms, but none change the course of the disease.

Lecanemab is an antibody - like those the body makes to attack viruses or bacteria - that has been engineered to tell the immune system to clear amyloid from the brain.

Amyloid is a protein that clumps together in the spaces between neurons in the brain and forms distinctive plaques that are one of the hallmarks of Alzheimer's.
"""

os.chdir(r'C:\공부\11가지 프로젝트로 시작하는 파이썬 생활 프로그래밍\Ch04')

Klist = re.split(r'\.',K)
Elist = re.split(r'\.',E)

total = []

for i in range(len(Elist)):
    total.append([Elist[i],Klist[i]])

usecsv.writecsv('K_E.csv', total)
