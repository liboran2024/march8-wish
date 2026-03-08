import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="3.8 Special Gift", page_icon="🌹", layout="centered")

# 2. 极致 UI 优化
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&family=Dancing+Script:wght@700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #ff6a88 100%);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 贺卡容器：毛玻璃质感 */
    .glass-card {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 32px;
        padding: 50px 35px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
        text-align: center;
        border: none;
        margin-top: 20px;
    }

    /* 方框内的标题：Happy 3.8 Day */
    .inner-banner {
        font-family: 'Dancing Script', cursive;
        font-size: 64px !important; /* 放大字号 */
        color: #ffffff;
        margin-bottom: 5px;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.4);
    }
    .inner-sub {
        font-family: 'Noto Sans SC', sans-serif;
        font-size: 18px;
        color: rgba(255, 255, 255, 0.8);
        letter-spacing: 6px;
        margin-bottom: 40px;
        text-transform: uppercase;
    }

    .main-desc {
        font-size: 26px !important;
        color: #ffffff;
        line-height: 1.6;
        margin-bottom: 40px;
        font-weight: 500;
    }

    /* 输入框样式 */
    .stTextInput>div>div {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 16px !important;
        border: none !important;
    }
    .stTextInput input {
        color: #333 !important;
        font-size: 20px !important;
    }

    /* 按钮样式 */
    .stButton>button {
        background: #ffffff !important;
        color: #764ba2 !important;
        border: none !important;
        padding: 12px 60px !important;
        font-size: 22px !important;
        border-radius: 50px !important;
        font-weight: 700 !important;
        transition: 0.3s all;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2) !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. 状态管理
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- 关卡逻辑 ---

# 所有的内容都放进这个 glass-card 容器
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# 每一页都显示的顶部招牌
st.markdown('<p class="inner-banner">Happy 3.8 Day</p>', unsafe_allow_html=True)
st.markdown('<p class="inner-sub">女神节·专属礼遇</p>', unsafe_allow_html=True)

if st.session_state.step == 1:
    st.markdown('<p class="main-desc">Hi, 今天是几月几日？<br><span style="font-size:16px; opacity:0.8;">(输入数字，开启你的专属惊喜)</span></p>', unsafe_allow_html=True)
    q1 = st.text_input("Date", placeholder="例如: 3.8", label_visibility="collapsed")
    if st.button("下一步"):
        if "3" in q1 and "8" in q1:
            st.session_state.step = 2
            st.rerun()
        else: st.error("日期似乎不对哦？")

elif st.session_state.step == 2:
    st.markdown('<p class="main-desc">让我猜猜，哪位女神<br>现在还在辛苦地加班？🤔</p>', unsafe_allow_html=True)
    q2 = st.text_input("Name", placeholder="输入名字", label_visibility="collapsed")
    if st.button("解锁心意"):
        if any(x in q2 for x in ["沈渊博", "我", "你自己"]):
            st.session_state.step = 3
            st.rerun()
        else: st.warning("名字不对哦，再试一次？")

elif st.session_state.step == 3:
    st.snow()
    st.markdown('<p class="main-desc">“ 愿你所有的努力，<br>都有温暖的回响。 ”</p>', unsafe_allow_html=True)
    st.markdown("<p style='color:white; font-size:20px; margin-bottom:40px;'>沈老师，加班辛苦啦。<br>喝杯温水，稍微休息一下。☕</p>", unsafe_allow_html=True)
    if st.button("继续"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.markdown('<p class="main-desc">“ 3月8日，<br>愿你始终闪闪发光。 ”</p>', unsafe_allow_html=True)
    st.markdown("<p style='color:white; font-size:20px; margin-bottom:40px;'>愿你做自己的女王，<br>不卑不亢，温柔且坚强。🌹</p>", unsafe_allow_html=True)
    if st.button("压轴惊喜"):
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.toast("🎇 旗开得胜！", icon="💖")
    st.balloons()
    st.markdown('<p class="main-desc" style="font-weight:700; color:#ffeaa7; font-size:32px !important;">祝下周公开课，<br>旗开得胜，圆满成功！</p>', unsafe_allow_html=True)
    st.markdown("<p style='color:white; font-size:22px; margin-bottom:40px;'>自信的你最迷人。<br>你是最棒的，为你加油！💪</p>", unsafe_allow_html=True)
    if st.button("回味一下"):
        st.session_state.step = 1
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # 闭合 glass-card