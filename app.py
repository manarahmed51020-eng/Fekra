
import streamlit as st

st.set_page_config(
    page_title="Fekra | فكرة",
    page_icon="💡",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}
.stApp {
    background-color: #0b1020;
    color: white;
}
h1, h2, h3, p, label {
    color: white;
}
div.stButton > button {
    background: #22c5df;
    color: #07111d;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

tools = [
    "اسألني",
    "برزنتيشن",
    "محول PDF",
    "إنفوجرافيك",
    "خريطة ذهنية",
    "فيديو بالذكاء الاصطناعي",
    "مونتاج",
    "إزالة الموسيقى",
    "صور بالذكاء الاصطناعي",
    "ملخص البحث",
    "كاتب المقالات",
    "تعليق صوتي",
    "تصميم بوستر",
    "بطاقات تعليمية",
    "صانع اختبارات",
    "سيرة ذاتية",
    "ترجمة",
    "حل واجبات",
    "خطة دراسة",
    "أداة إضافية"
]

st.sidebar.title("💡 فكرة Fekra")
page = st.sidebar.radio(
    "القائمة الرئيسية",
    ["الرئيسية", "أدوات الذكاء الاصطناعي", "المدونة"]
)

if page == "الرئيسية":
    st.title("💡 Fekra | فكرة")
    st.subheader("حوّل أفكارك إلى إبداع")

    st.write(
        "منصة تجمع أدوات الذكاء الاصطناعي "
        "لمساعدتك على التعلم والإبداع وإنجاز أعمالك."
    )

    st.divider()

    st.header("ماذا يمكنك أن تفعل في فكرة؟")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🎬 إنشاء الفيديوهات")

    with col2:
        st.info("🖼️ التصميم والإبداع")

    with col3:
        st.info("📚 التعلم والكتابة")

    st.write("اكتشف أدوات فكرة وابدأ تنفيذ أفكارك.")

elif page == "أدوات الذكاء الاصطناعي":
    st.title("أدوات الذكاء الاصطناعي")
    selected_tool = st.selectbox(
        "اختاري الأداة التي تريدين استخدامها",
        tools
    )

    st.subheader(selected_tool)
    st.write("مساحة العمل الخاصة بأداة " + selected_tool)

    user_input = st.text_area(
        "اكتبي طلبك أو فكرتك هنا:"
    )

    if st.button("تنفيذ الطلب"):
        if user_input.strip():
            st.success(
                "تم استلام طلبك. سيتم ربط هذه الأداة "
                "بخدمة الذكاء الاصطناعي الخاصة بها لاحقاً."
            )
        else:
            st.warning("اكتبي طلبك أولاً.")

elif page == "المدونة":
    st.title("مدونة فكرة")
    st.write("مساحة المقالات والمعرفة والإبداع.")

    st.subheader("مرحباً بك في مدونة Fekra")
    st.write(
        "هنا سننشر مقالات أصلية عن الذكاء الاصطناعي "
        "والتعلم والتكنولوجيا والإبداع."
    )

st.divider()
st.caption("Fekra | فكرة - مشروع قيد التطوير")
