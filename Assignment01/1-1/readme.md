# 1-1. Quick Sort 분석 및 최적화

## Hands-on assignment 1-1: Quick Sort
Problem definition: We have an unsorted array: [21, 3, 12, 15, 7, 32, 4, 25, 9, 18]. Let’s sort it using a quick sort algorithm, but this time, you will evaluate how an AI handles it.
- Step 1 (Generate): Ask an AI (ChatGPT, Gemini, etc.) to write a standard Quick Sort algorithm with the pivot selection picking the first element. Document the exact prompt you used and the AI's generated code.
- Step 2 (Analyze & Break): Based on the AI's pivot selection strategy, design an adversarial input array (a specific sequence of numbers) that will force this AI-generated code to degrade to its worst-case Θ 𝑛2    time complexity.
-Requirement: Add a counter variable to the AI's code to count the exact number of recursive calls or comparisons to prove it runs in Θ 𝑛2    on your adversarial array.
- Step 3 (Optimize): Prompt the AI again (or manually refactor the code) to implement an optimized Quick Sort that achieves Θ 𝑛𝑙𝑜𝑔𝑛  time complexity even on your adversarial array.
- Step 4 (Report): Briefly explain why the first AI code failed efficiency standards on your adversarial input, and why the optimized version successfully mitigated the issue.

---
**대상 배열**: [21, 3, 12, 15, 7, 32, 4, 25, 9, 18]

- Step 1 (생성): AI에게 "첫 번째 요소를 피벗(pivot)으로 선택하는 표준 퀵 정렬 코드를 작성해달라"고 요청합니다. 사용한 프롬프트와 결과 코드를 기록하세요.

- Step 2 (분석 및 파괴): AI가 선택한 피벗 전략을 바탕으로, 이 코드의 시간 복잡도를 최악의 경우인 $\Theta(n^2)$으로 만드는 **최악의 입력 배열(Adversarial Input)**을 설계하세요.

    * 요구사항: AI 코드에 카운터 변수를 추가하여 재귀 호출 횟수나 비교 횟수를 측정하고, 실제로 $\Theta(n^2)$이 나옴을 증명하세요.

- Step 3 (최적화): AI에게 다시 요청하거나 직접 코드를 수정하여, 최악의 입력에서도 $\Theta(n \log n)$을 유지하는 최적화된 퀵 정렬을 구현하세요.

- Step 4 (보고서): 첫 번째 AI 코드가 왜 최악의 입력에서 효율성 기준을 통과하지 못했는지, 그리고 최적화된 버전은 어떻게 문제를 해결했는지 설명하세요.

