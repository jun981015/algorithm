import bisect
from collections import defaultdict
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    INFO = [['cpp','python','java'],['frontend','backend'],['junior','senior'],['pizza','chicken']]
    for i in info:
        _ = i.split()
        key = ''.join(_[:4])
        info_dict[key].append(int(_[-1]))
        info_dict[key].sort()
    for _ in query:
        check = _.replace('and','').split()
        check ,score= check[:-1],int(check[-1])
        checklist = ['']
        for c,I in zip(check,INFO):
                checklist = [exi + add for exi in checklist for add in I] if c=='-' else [exi+c for exi in checklist]
        answer.append(sum([len(info_dict[i]) - bisect.bisect_left(info_dict[i],score) for i in checklist if i in info_dict]))
    return answer