import streamlit as st
import pandas as pd

st.set_page_config(page_title="국가별 MBTI 분포 🌍", page_icon="🌐", layout="centered")

st.title("🌍 국가별 MBTI 분포 비교")
st.caption("🗺️ 전 세계 주요 국가들의 MBTI 성향과 차이를 확인해 보세요.")
st.divider()

# 세계 주요 국가 MBTI 샘플 데이터
world_mbti_data = {
    "대한민국 🇰🇷": {"ISTJ": 14.7, "ESTJ": 10.2, "ENFP": 9.5, "ISFP": 8.6, "ISFJ": 8.1, "기타": 48.9},
    "미국 🇺🇸": {"ISFJ": 13.8, "ESFJ": 12.3, "ISTJ": 11.6, "ISFP": 8.8, "ESTJ": 8.7, "기타": 44.8},
    "일본 🇯🇵": {"INFP": 12.5, "ENFP": 11.2, "INTP": 9.4, "ISFP": 8.3, "ISTJ": 8.0, "기타": 50.6},
    "독일 🇩🇪": {"ISTJ": 15.2, "ESTJ": 11.8, "INTJ": 8.4, "INTP": 7.9, "ISFJ": 7.5, "기타": 49.2},
    "영국 🇬🇧": {"ISFJ": 12.9, "ISTJ": 12.1, "ESFJ": 10.4, "ENFP": 8.9, "ISFP": 8.1, "기타": 47.6}
}

# 국가 선택 드롭다운
selected_country = st.selectbox(
    "👇 **궁금한 국가를 선택하세요:**",
    list(world_mbti_data.keys())
)

st.write("")

if selected_country:
    country_data = world_mbti_data[selected_country]
    
    st.subheader(f"📊 {selected_country} 상위 MBTI 분포")
    
    # 데이터프레임 변환 후 차트 출력
    df_country = pd.DataFrame(
        list(country_data.items()),
        columns=["MBTI 유형", "비율(%)"]
    ).set_index("MBTI 유형")
    
    st.bar_chart(df_country)
    
    st.write("---")
    st.markdown("### 🗣️ 국가별 문화와 MBTI 이야기")
    
    if "대한민국" in selected_country:
        st.write("🇰🇷 **성실함과 신뢰:** 조직에 대한 책임감(ST)과 트렌디한 창의성(N/FP)이 조화를 이루는 문화입니다.")
    elif "미국" in selected_country:
        st.write("🇺🇸 **사교성과 실용성:** 사람들과의 네트워크와 공동체를 중시하는 SFJ 유형이 높게 나타납니다.")
    elif "일본" in selected_country:
        st.write("🇯🇵 **내면의 감성과 사고:** 배려와 타인에 대한 의식, 내면의 아이디어를 중시하는 IN 계열이 상대적으로 높습니다.")
    elif "독일" in selected_country:
        st.write("🇩🇪 **원칙과 시스템:** 철저한 기획과 체계적인 질서를 선호하는 TJ 유형이 강세를 보입니다.")
    elif "영국" in selected_country:
        st.write("🇬🇧 **전통과 유대감:** 전통적 가치를 존중하며 안정적인 관계를 추구하는 S/J 성향이 우세합니다.")

st.divider()
st.info("💡 **상담가의 조언:** 문화적 배경과 교육 환경에 따라 국가마다 우세한 MBTI 성향이 조금씩 다를 수 있답니다!")