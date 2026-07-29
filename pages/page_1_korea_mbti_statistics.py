import streamlit as st
import pandas as pd

st.set_page_config(page_title="한국인 MBTI 비율 🇰🇷", page_icon="📊", layout="centered")

st.title("🇰🇷 우리나라 한국인 MBTI 비율 분석")
st.caption("📊 국내 통계 데이터를 기반으로 한 한국인의 MBTI 분포 그래프입니다.")
st.divider()

# 한국인 MBTI 비율 데이터 (단위: %)
korea_mbti_data = {
    "MBTI": [
        "ISTJ", "ESTJ", "ENFP", "ISFP", "ISFJ",
        "INFP", "ESFJ", "INTJ", "INTP", "INFJ",
        "ISTP", "ESFP", "ENTP", "ENFJ", "ESTP", "ENTJ"
    ],
    "비율(%)": [
        14.7, 10.2, 9.5, 8.6, 8.1,
        7.2, 6.8, 5.5, 5.1, 4.8,
        4.7, 4.5, 3.8, 3.1, 2.3, 1.2
    ]
}

df_korea = pd.DataFrame(korea_mbti_data)
df_korea_chart = df_korea.set_index("MBTI")

st.subheader("📈 MBTI 유형별 분포 그래프")
# 별도 차트 라이브러리 없이 Streamlit 내장 bar_chart 활용
st.bar_chart(df_korea_chart["비율(%)"])

st.divider()

# 주요 통계 하이라이트
st.subheader("🔍 상담가가 들려주는 한국인 MBTI 특징")

col1, col2 = st.columns(2)

with col1:
    st.success("🥇 **가장 많은 유형 TOP 3**")
    st.write("1. **ISTJ** (14.7%) - 신중한 현실주의자")
    st.write("2. **ESTJ** (10.2%) - 엄격한 관리자")
    st.write("3. **ENFP** (9.5%) - 재발굴의 활동가")

with col2:
    st.warning("💎 **희귀한 유형 TOP 3**")
    st.write("1. **ENTJ** (1.2%) - 대담한 지도자")
    st.write("2. **ESTP** (2.3%) - 수완 좋은 활동가")
    st.write("3. **ENFJ** (3.1%) - 정의로운 언변가")

st.write("")
st.info(
    """
    💡 **상담가의 인사이트:**
    
    우리나라는 전통적으로 규칙과 정돈, 책임감을 중시하는 **SJ 계열(ISTJ, ESTJ, ISFJ 등)**의 비율이 높게 나타납니다.
    하지만 최근 청소년 및 젊은 층에서는 **ENFP, INFP** 등 자아 표현과 창의성을 중시하는 유형도 크게 증가하고 있답니다!
    """
)