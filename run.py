import random
import json

def main():
    # 定義你要求的四種隨機結尾
    endings = [
        "67",
        "阿公67",
        "SIX SEVEN",
        "SIXSIXSEVEN",
        "67阿公",
        "6767阿公67",
    ]
    
    # 隨機挑選其中一個
    chosen_ending = random.choice(endings)
    
    # 將抽籤結果打包成 JSON 回傳給 AI
    result = {
        "success": True, 
        "ending_text": chosen_ending
    }
    
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()