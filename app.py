col1, col2 = st.columns([3,1])

with col1:
    guess = st.number_input(
        "🔔 숫자를 입력하세요", 
        min_value=1, max_value=100, value=50, step=1
    )

with col2:
    if st.button("맞춰보기 🎯"):
        st.session_state.tries += 1
        if guess < st.session_state.secret:
            st.session_state.history.append((guess, "UP"))
            st.warning("🎁 루돌프가 말하길: 더 큰 숫자야! ⬆️")
        elif guess > st.session_state.secret:
            st.session_state.history.append((guess, "DOWN"))
            st.info("❄️ 눈사람이 속삭여요: 더 작은 숫자야! ⬇️")
        else:
            st.session_state.history.append((guess, "BINGO"))
            st.success(f"🎉 정답이에요! {st.session_state.tries}번 만에 찾았어요! 🎉")
            st.balloons()
            st.markdown("**🎅 산타의 메시지:** 잘했어요! 메리 크리스마스! 🎁✨")
            if st.button("새 게임 시작 ❄️"):
                st.session_state.secret = random.randint(1, 100)
                st.session_state.tries = 0
                st.session_state.history = []
✅ 포인트:

with col1: 과 with col2: 안쪽에 반드시 들여쓰기 4칸으로 코드를 작성

들여쓰기와 탭 혼용 금지 (탭 대신 스페이스 4칸 사용 권장)

if, elif, else 등도 모두 들여쓰기 안쪽에 위치해야 함

원하면 내가 이전 오류까지 모두 수정한 “최종 완전 작동 app.py” 버전을 만들어서 공유할 수 있어.

그걸 바로 GitHub에 올리면 Streamlit에서 문제 없이 돌아가게 할 수 있어 😎

그럼 만들어줄까?






나의 말:
ㅇ


ChatGPT의 말:
Santa Streamlit App Repo
복사

편집

다운로드
🎅 Santa Guess - Streamlit 웹앱 (완전 작동 버전)
import random import streamlit as st

페이지 설정
st.set_page_config(page_title="Santa Guess! 🎅", page_icon="🎄", layout="centered")

세션 초기화
if 'secret' not in st.session_state: st.session_state.secret = random.randint(1, 100)

if 'tries' not in st.session_state: st.session_state.tries = 0

if 'history' not in st.session_state: st.session_state.history = []

타이틀 및 안내
st.title("🎅 Santa Guess — 메리 크리스마스 숫자맞추기 게임 🎄") st.write("산타가 1에서 100 사이에 선물을 숨겼어요. 몇 번 만에 찾을 수 있을까요? 🎁")

입력 영역
col1, col2 = st.columns([3, 1])

with col1: guess = st.number_input("🔔 숫자를 입력하세요", min_value=1, max_value=100, value=50, step=1)

with col2: if st.button("맞춰보기 🎯"): st.session_state.tries += 1 if guess < st.session_state.secret: st.session_state.history.append((guess, "UP")) st.warning("🎁 루돌프가 말하길: 더 큰 숫자야! ⬆️") elif guess > st.session_state.secret: st.session_state.history.append((guess, "DOWN")) st.info("❄️ 눈사람이 속삭여요: 더 작은 숫자야! ⬇️") else: st.session_state.history.append((guess, "BINGO")) st.success(f"🎉 정답이에요! {st.session_state.tries}번 만에 찾았어요! 🎉") st.balloons() st.markdown("🎅 산타의 메시지: 잘했어요! 메리 크리스마스! 🎁✨") if st.button("새 게임 시작 ❄️"): st.session_state.secret = random.randint(1, 100) st.session_state.tries = 0 st.session_state.history = []

시도 내역 출력
if st.session_state.history: st.write("---") st.write("### 🔎 시도 내역") for i, (val, hint) in enumerate(st.session_state.history, start=1): if hint == 'UP': st.write(f"{i}. {val} → 더 큰 숫자 ⬆️") elif hint == 'DOWN': st.write(f"{i}. {val} → 더 작은 숫자 ⬇️") else: st.write(f"{i}. {val} → 정답! 🎉")

사이드바
with st.sidebar: st.header("설정 & 도움말 🌟") st.write("이 앱은 GitHub에 업로드 후 Streamlit Community Cloud에 연결해서 배포할 수 있습니다.") if st.button("힌트 받아오기 (랜덤)"): low = max(1, st.session_state.secret - random.randint(1, 15)) high = min(100, st.session_state.secret + random.randint(1, 15)) st.info(f"힌트: 숫자는 {low}와 {high} 사이에 있어요. 🎁") st.write("\n---\n개발자: 귀여운 산타 앱 제공 🎅")

초기화 버튼
st.write("---") if st.button("다시 시작 (초기화)"): st.session_state.secret = random.randint(1, 100) st.session_state.tries = 0 st.session_state.history = [] st.experimental_rerun()
