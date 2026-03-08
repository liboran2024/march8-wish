import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="Special Surprise", page_icon="🌹", layout="centered")

# 2. 高级 UI 注入 (核心：毛玻璃效果 & 优雅过渡)
st.markdown("""
    <style>
    /* 引入 Google 艺术字体 */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Noto+Sans+SC:wght@300;500&display=swap');

    /* 全局背景：流动的梦幻粉紫 */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 贺卡主体：毛玻璃质感 */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 40px;
        margin-top: 20px;
        animation: fadeInUp 1s ease-out;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 文字样式 */
    .title-text {
        font-family: 'Dancing Script', cursive;
        font-size: 50px;
        color: white;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .main-desc {
        font-family: 'Noto Sans SC', sans-serif;
        font-weight: 300;
        color: #ffffff;
        font-size: 20px;
        text-align: center;
        line-height: 1.8;
        margin-bottom: 30px;
    }

    /* 苹果风按钮 */
    .stButton>button {
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        border-radius: 12px !important;
        padding: 10px 40px !important;
        transition: 0.3s all !important;
        backdrop-filter: blur(5px);
        font-size: 18px !important;
    }
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.4) !important;
        transform: scale(1.05);
        border: 1px solid white !important;
    }

    /* 输入框样式微调 */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 逻辑控制
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- 关卡渲染 ---

# 每一层都用 container 包裹以应用动画
container = st.container()

with container:
    if st.session_state.step == 1:
        st.markdown('<p class="title-text">Step 01</p>', unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<p class="main-desc">Hi, 今天是几月几日？<br><small>(输入数字即可)</small></p>', unsafe_allow_html=True)
        q1 = st.text_input("Date", placeholder="0308", label_visibility="collapsed")
        if st.button("进入惊喜通道 →"):
            if "3" in q1 and "8" in q1:
                st.session_state.step = 2
                st.rerun()
            else: st.error("日期不对哦，惊喜还没准备好呢~")
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.step == 2:
        st.markdown('<p class="title-text">Step 02</p>', unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<p class="main-desc">让我猜猜...<br>谁现在还在辛苦地加班？🤔</p>', unsafe_allow_html=True)
        q2 = st.text_input("Name", placeholder="请输入名字", label_visibility="collapsed")
        if st.button("锁定目标"):
            if any(x in q2 for x in ["沈渊博", "我", "你自己"]):
                st.session_state.step = 3
                st.rerun()
            else: st.warning("这位同学似乎不在加班名单上呢...")
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.step == 3:
        st.markdown('<p class="title-text">For You</p>', unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<p class="main-desc">“ 愿你所有的努力，<br>都有温暖的回响。 ”</p>', unsafe_allow_html=True)
        st.write("---")
        st.write("沈老师，加班辛苦啦。喝杯水，放松一下眼睛吧。")
        if st.button("继续开启 →"):
            st.session_state.step = 4
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.step == 4:
        st.markdown('<p class="title-text">Happy Day</p>', unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<p class="main-desc">“ 3月8日，<br>愿你始终闪闪发光。 ”</p>', unsafe_allow_html=True)
        st.write("---")
        st.write("不论在哪，你都是那个最独立、最自信的女神。")
        if st.button("查看最后的祝福 →"):
            st.session_state.step = 5
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.step == 5:
        st.balloons()
        st.markdown('<p class="title-text">Best Wishes</p>', unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<p class="main-desc" style="font-weight:700;">“ 祝下周公开课，<br>旗开得胜，圆满成功！ ”</p>', unsafe_allow_html=True)
        st.write("---")
        st.write("全场最稳是你，最棒也是你。我在后方为你疯狂打 Call！📣")
        if st.button("重新开始"):
            st.session_state.step = 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)