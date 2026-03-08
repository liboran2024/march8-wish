import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="沈渊博节日快乐", page_icon="🌹", layout="centered")

# 2. 极致 UI 优化 (消除毛边，填充内容，增强质感)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&family=Dancing+Script:wght@700&display=swap');

    /* 极高饱和度的深邃渐变背景 */
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

    /* 贺卡容器：彻底消除毛边，增强平滑度 */
    .glass-card {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 32px;
        border: none; /* 彻底移除毛边 */
        padding: 50px 35px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
        text-align: center;
        margin-top: 10px;
    }

    /* 顶部填充内容：3.8 节日快乐艺术字 */
    .top-banner {
        font-family: 'Dancing Script', cursive;
        font-size: 48px;
        color: #ffffff;
        margin-bottom: 20px;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
    }
    .top-sub {
        font-family: 'Noto Sans SC', sans-serif;
        font-size: 16px;
        color: rgba(255, 255, 255, 0.8);
        letter-spacing: 4px;
        margin-bottom: 30px;
    }

    /* 文字字体与大小 */
    .title-text {
        font-size: 38px !important;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 20px;
    }
    .main-desc {
        font-size: 24px !important;
        color: #ffffff;
        line-height: 1.6;
        margin-bottom: 40px;
        font-weight: 400;
    }

    /* 对话框/输入框重设计：极简纯净 */
    .stTextInput>div>div {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 16px !important;
        border: none !important; /* 移除外框毛边 */
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
    }
    .stTextInput input {
        color: #333 !important;
        font-size: 18px !important;
        padding: 12px !important;
    }

    /* 按钮：Apple 风格扁平化 */
    .stButton>button {
        background: #ffffff !important;
        color: #764ba2 !important;
        border: none !important;
        padding: 12px 50px !important;
        font-size: 20px !important;
        border-radius: 50px !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.2) !important;
        background: #f8f9fa !important;
    }

    /* 隐藏 Streamlit 默认的页眉页脚，保持纯净 */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. 状态管理
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- 关卡逻辑 ---

# 顶部常驻标语 (解决方框空白问题)
st.markdown('<div style="text-align:center;"><p class="top-banner">Happy 3.8 Day</p><p class="top-sub">女神节·专属礼遇</p></div>', unsafe_allow_html=True)

if st.session_state.step == 1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Step 01</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">Hi, 今天是几月几日？<br><span style="font-size:16px; opacity:0.8;">(提示：一个浪漫的数字组合)</span></p>', unsafe_allow_html=True)
    q1 = st.text_input("Date", placeholder="在此输入日期", label_visibility="collapsed")
    if st.button("下一步"):
        if "3" in q1 and "8" in q1:
            st.session_state.step = 2
            st.rerun()
        else: st.error("看来还没进入过节状态哦？")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Step 02</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">让我猜猜，哪位女神<br>现在还在辛苦地加班？🤔</p>', unsafe_allow_html=True)
    q2 = st.text_input("Name", placeholder="请输入Ta的名字", label_visibility="collapsed")
    if st.button("解锁心意"):
        if any(x in q2 for x in ["沈渊博", "我", "你自己"]):
            st.session_state.step = 3
            st.rerun()
        else: st.warning("名字输入有误，再确认一下？")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 3:
    st.snow()
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Phase 01</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">“ 愿你所有的努力，<br>都有温暖的回响。 ”</p>', unsafe_allow_html=True)
    st.markdown("<p style='color:rgba(255,255,255,0.9); font-size:18px;'>沈老师，加班辛苦啦。<br>放下手头的工作，深呼吸一下。☕</p>", unsafe_allow_html=True)
    if st.button("继续"):
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 4:
    st.balloons()
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Phase 02</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">“ 3月8日，<br>愿你始终闪闪发光。 ”</p>', unsafe_allow_html=True)
    st.markdown("<p style='color:rgba(255,255,255,0.9); font-size:18px;'>愿你做自己的女王，<br>不卑不亢，温柔且坚强。🌹</p>", unsafe_allow_html=True)
    if st.button("压轴惊喜"):
        st.session_state.step = 5
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 5:
    st.toast("🎇 全力以赴！", icon="💖")
    st.toast("🚀 凯旋而归！", icon="🔥")
    st.balloons()
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Best Wish</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc" style="font-weight:700; color:#ffeaa7;">“ 祝下周公开课，<br>旗开得胜，圆满成功！ ”</p>', unsafe_allow_html=True)
    st.markdown("<p style='color:rgba(255,255,255,0.9); font-size:22px;'>你专注的样子最有魅力。<br>你是最棒的，我们都为你加油！💪</