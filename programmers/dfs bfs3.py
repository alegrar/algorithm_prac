# 프로그래머스 # dfs bfs # '단어 변환'

def solution(begin, target, words):
    answer = 0
    word_size = len(begin)
    alphabet_lst = {}
    check = {i:0 for i in words}
    
    def dfs(this_word, cnt, min_cnt, vocab):
        if this_word == target :
            min_cnt = min(min_cnt, cnt)
            return min_cnt

        if cnt == len(words):
            return 0
        
        
        for i_key in range(len(alphabet_lst)):
            for letters_idx in range(len(alphabet_lst[i_key])) : 
                temp_word = list(this_word)
                temp_word[i_key] = alphabet_lst[i_key][letters_idx]
                temp_word = ''.join(temp_word)
                # print(temp_word)
                if temp_word in words and not check[temp_word]: 
                    cnt += 1
                    check[temp_word] = 1
                    vocab.append(temp_word)
                    min_cnt = dfs(temp_word, cnt, min_cnt, vocab)
                    vocab.pop()
                    cnt -= 1
                    check[temp_word] = 0
        return min_cnt


    for i in range(word_size):
        alphabet = set()
        for word in words:
            alphabet.add(word[i])
        alphabet_lst[i] = list(alphabet) 
    # print(alphabet_lst)
    # {0: ['h', 'l', 'd', 'c'], 1: ['o'], 2: ['g', 't']}

    if target not in words :
        return 0

    vocab = []
    answer = dfs(begin, 0, len(words), vocab)

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "cot", "cog"]
# ["hot", "dot", "dog", "lot", "log", "cog"]
# ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))
