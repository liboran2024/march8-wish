import streamlit as st
import time
import random

# 1. 页面配置
st.set_page_config(page_title="Special Surprise", page_icon="🎁", layout="centered")

# 2. 大厂风 UI 设计 (毛玻璃效果 & 优雅字体)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
    }
    /* 玻璃拟态卡片 */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 20px;
    }
    /* 苹果风格的大按钮 */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        border: none;
        background-color: #ec407a;
        color: white;
        height: 3em;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #d81b60;
        transform: translateY(-2px);
    }
    h1, h2, h3 {
        color: #880e4f !important;
        font-family: 'PingFang SC', 'Helvetica Neue', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 状态管理
if 'stage' not in st.session_state:
    st.session_state.stage = 'q1'

# --- 第一层：整蛊答题（日期） ---
if st.session_state.stage == 'q1':
    st.markdown("<div class='glass-card'><h2>第一关：考验默契的时候到了</h2>", unsafe_allow_html=True)
    q1 = st.text_input("今天是几月几日？（这都答错就准备搓衣板吧😏）", placeholder="例如：3月8日")
    if st.button("提交答案"):
        if "3" in q1 and "8" in q1:
            st.success("算你识相，过关！")
            time.sleep(1)
            st.session_state.stage = 'q2'
            st.rerun()
        else:
            st.error("日期都能记错？再给你一次机会！")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 第二层：整蛊答题（加班） ---
elif st.session_state.stage == 'q2':
    st.markdown("<div class='glass-card'><h2>第二关：让我猜猜...</h2>", unsafe_allow_html=True)
    st.write("让我猜猜今天谁还在苦逼地加班，好难猜啊... 🤔")
    q2 = st.text_input("请输入那个加班狂的名字：", placeholder="提示：远在天边近在眼前")
    if st.button("确定是Ta吗？"):
        if any(name in q2 for name in ["沈渊博", "我", "你自己"]):
            st.success("哈哈哈哈，真相了！这就为你开启补偿模式~")
            time.sleep(1.5)
            st.session_state.stage = 'wish1'
            st.rerun()
        else:
            st.warning("虽然Ta可能也在加班，但不是我要的那个答案哦~")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 祝福页面：第一层（工作快乐） ---
elif st.session_state.stage == 'wish1':
    st.snow() # 意境雪花
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.title("💼 Level 1: 能量补给")
    st.subheader("辛苦啦！加班的小仙女")
    st.write("知道你现在还在工位上奋斗，希望这些文字能给你充点电：")
    st.info("“愿你的工作只有成就感，没有疲惫感；代码一遍过，方案不被改！”")
    if st.button("点击领取下一份惊喜 →"):
        st.session_state.stage = 'wish2'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 祝福页面：第二层（妇女节快乐） ---
elif st.session_state.stage == 'wish2':
    st.balloons() # 气球雨
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.title("🌹 Level 2: 女神专属")
    st.subheader("3月8日，你最闪耀")
    st.write("不仅是今天，愿你每一天都能活得热烈而自在。")
    st.success("“妇女节快乐！去做那个不被定义的、最好的自己。”")
    if st.button("最后一份惊喜，请查收 →"):
        st.session_state.stage = 'wish3'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 祝福页面：第三层（公开课顺利） ---
elif st.session_state.stage == 'wish3':
    # 烟花/爱心雨效果 (Streamlit 自带气球和雪花，爱心可以用 emoji 动画模拟)
    st.toast("❤️❤️❤️❤️❤️❤️❤️❤️", icon="💖")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.title("🎯 Level 3: 旗开得胜")
    st.subheader("下周公开课特辑")
    st.write("压轴的祝福送给下周最重要的事情：")
    st.markdown("""
        ### 📢 **祝：公开课大圆满！**
        全场最稳是你，最自信也是你。<br>
        别紧张，你准备得那么充分，一定会惊艳全场的！<br>
        我在后方为你疯狂打 call 📣
    """, unsafe_allow_html=True)
    
    if st.button("重新开始仪式"):
        st.session_state.stage = 'q1'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)