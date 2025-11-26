import random
import streamlit as st


# 페이지 설정
st.set_page_config(page_title="Santa Guess! 🎅", page_icon="🎄", layout="centered")


# 초기화
if 'secret' not in st.session_state:
st.session_state.secret = random.randint(1, 100)
if 'tries' not in st.session_state:
st.session_state.tries = 0
if 'history' not in st.session_state:
st.session_state.history = []


st.title("🎅 Santa Guess — 메리 크리스마스 숫자맞추기 게임 🎄")
st.write("산타가 1에서 100 사이에 선물을 숨겼어요. 몇 번 만에 찾을 수 있을까요? 🎁")


col1, col2 = st.columns([3,1])
with col1:
guess = st.number_input("🔔 숫자를 입력하세요", min_value=1, max_value=100, value=50, step=1)
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


# 히스토리와 팁
if st.session_state.history:
st.write("---")
st.write("### 🔎 시도 내역")
for i, (val, hint) in enumerate(st.session_state.history, start=1):
if hint == 'UP':
st.write(f"{i}. {val} → 더 큰 숫자 ⬆️")
elif hint == 'DOWN':
st.write(f"{i}. {val} → 더 작은 숫자 ⬇️")
else:
st.write(f"{i}. {val} → 정답! 🎉")


# 사이드바 (설정)
with st.sidebar:
st.header("설정 & 도움말 🌟")
st.write("이 앱은 GitHub에 업로드 후 Streamlit Community Cloud에 연결해서 배포할 수 있습니다.")
if st.button("힌트 받아오기 (랜덤)"):
# 간단한 확률 기반 힌트
low = max(1, st.session_state.secret - random.randint(1, 15))
high = min(100, st.session_state.secret + random.randint(1, 15))
st.info(f"힌트: 숫자는 {low}와 {high} 사이에 있어요. 🎁")
st.write("\n---\n개발자: 귀여운 산타 앱 제공 🎅")
st.experimental_rerun()
