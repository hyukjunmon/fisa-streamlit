import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

title = st.text_input("애니메이션 제목을 입력해주세요.", key="ani")

if title in ani_list:
    index = ani_list.index(title)
    st.image(img_list[index], caption=title, width=200)
else:
    if title != "":
        st.write(f"{st.session_state.ani}라는 애니메이션은 없습니다.")
    for title in ani_list:
        index = ani_list.index(title)
        st.image(img_list[index], caption=title, width=200)