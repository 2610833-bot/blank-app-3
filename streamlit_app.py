import streamlit as st

# 앱 제목 설정
st.title("🍿 영화관 세트메뉴 조합기")
st.subheader("선택할 수 있는 모든 세트메뉴 라인업입니다.")
st.write("---")

# 기존 데이터 및 반복문 유지
popcorn_options = ["기본", "캐라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

# 반복문을 돌며 스트림릿 화면에 출력
for popcorn in popcorn_options:
    for drink in drink_options:
        # st.success나 st.info를 쓰면 박스 형태로 예쁘게 출력됩니다.
        st.write(f"🎬 **세트메뉴:** {popcorn} 팝콘, {drink}")

st.write("---")
st.caption("원하시는 조합을 골라보세요!")