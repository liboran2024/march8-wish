import streamlit as st
import time
import random

# 1. 页面配置：设置一个心动的标题和图标
st.set_page_config(page_title="致最特别的你", page_icon="💖", layout="centered")

# 2. 注入自定义 CSS：改变背景颜色和字体
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    .main-title {
        color: white;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
        font-family: 'Microsoft YaHei';
    }
    .wish-text {
        font-size: 20px;
        color: #d63384;
        background: rgba(255, 255, 255, 0.6);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #d63384;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 初始界面
if 'step' not in st.session_state:
    st.session_state.step = 1

# 第一步：神秘入口
if st.session_state.step == 1:
    st.markdown("<h1 class='main-title'>🔒 收到一份加密的讯息</h1>", unsafe_allow_html=True)
    password = st.text_input("请输入暗号（提示：你的名字是...）", type="password")
    if st.button("解密 🔓"):
        if password == "沈渊博" or password == "308":  # 这里改写你俩的梗
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("暗号不对哟，再试一次？")

# 第二步：仪式感加载
elif st.session_state.step == 2:
    st.markdown("<h1 class='main-title'>正在同步心跳频率...</h1>", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    st.session_state.step = 3
    st.rerun()

# 第三步：正式祝福界面
elif st.session_state.step == 3:
    st.balloons()  # 撒气球
    st.markdown("<h1 class='main-title'>🌹 3.8 女神节快乐！</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='wish-text'>
    亲爱的：<br>
    在这个特别的日子里，不想只祝你节日快乐，<br>
    更想祝你每天都能随心所欲，活出最灿烂的自己。<br>
    你是我的专属星辰，永远闪闪发光。✨
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # 交互小彩蛋：点一下换一个赞美
    compliments = [
        "今天的你比昨天更迷人！💃",
        "你的笑容是全世界最有效的治愈剂。🌸",
        "愿你眼中总有星辰，心中总有大海。🌊",
        "做自己的女王，不卑不亢，温柔而有力量。👑"
    ]
    
    if st.button("点击抽取今日份赞美词"):
        st.write(f"### {random.choice(compliments)}")
        st.snow() # 撒点雪花增加浪漫感

    # 如果有合照，可以解除注释并替换 URL
    # st.image("https://example.com/your-photo.jpg", caption="定格美好时刻")