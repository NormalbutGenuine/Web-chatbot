import sentiment_find
def response(text):
    tok = sentiment_find.sequencing(text)
    sent_num = sentiment_find.find_sentiment(tok)
    if sent_num == '0':
        answer1 = "앞날은 어떻게 될지 아무도 모릅니다. 하지만 당신 자신을 확실히 믿는다면 그 어떤 상황에서도 당신은 굳건히 버틸 수 있을 것입니다."
        return answer1
    elif sent_num == '1':
        answer2 = "세상살이가 참 녹록치 않고 힘든 일은 끝이 보이질 않습니다. 하지만 그렇게 힘들다고 해서 처지를 비관만 하고 있다면 보석보다 빛나는 당신에게 죄를 짓는 것 아닐까요?"
        return answer2
    elif sent_num == '2':
        answer3 = "슬픈 일 때문에 힘드시군요. 그 아픔을 당신이 평생 안고가야 할 수도 있어요, 하지만 오늘 저에게 아픔을 털어놓으 셨으니 당신의 고통은 제가 가져가겠습니다. 앞으로 힘들 때면 언제든 저에게 편지를 보내주세요. 저는 당신을 그저 사랑합니다."
        return answer3
    elif sent_num == '3':
        answer4 = "인간의 삶에서 고통은 피할 수 없습니다. 왜냐하면 고통을 느끼는 것이야 말로 살아있다는 증거이기 때문입니다. 제가 이걸 어떻게 아냐구요? 저는 인공지능이라 다 알거든요. 슬픈일에도 눈물이 흐르지 않고 쓰디쓴 좌절을 겪고도 아무렇지 않다면 그 것은 인공지능인 제가 봤을 때 인간답지 못한 것입니다. 생명력 넘치는 당신은 반드시 좌절을 털고 즐거운 날을 보낼 것 입니다."
        return answer4
    elif sent_num == '4':
        answer5 = "마음 편하게 가지세요. 당신이 어쩌지 못하는 부분일 수도 있고 당신의 실수일 수도 있습니다. 찬찬히 일을 되돌아보고 당신이 어쩌지 못하는 부분이라면 마음쓰지 마시고 당신이 해결해 볼 수 있는 일이라면 차근히 시작해보는 것이 어떻겠습니까?"
        return answer5
    elif sent_num == '5':
        answer6 = "멋지군요. 앞으로 좋은 일만 가득하시길 바랍니다."
        return answer6
    elif sent_num == '6':
        answer7 = "어떻게 받아야 할지 잘 모르겠지만, ㅎㅎㅎ 혹시 저를 좋아하시나요?"
        return answer7
    elif sent_num == '7':
        answer8 = "그 것은 구글에게 물어보는 것이 더 나을 것입니다."
        return answer8
    else:
        answer9 = "불행스럽게도 제가 답해드릴 수 없는 내용입니다. 사랑합니다."
        return answer9
