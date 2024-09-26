import streamlit as st

st.title("Máy tính của Kiều Nga")

num1 = st.text_input("Nhập số thứ nhất")
operation = st.selectbox("Chọn phép tính", ("Cộng", "Trừ", "Nhân", "Chia"))
num2 = st.text_input("Nhập số thứ hai")

if st.button("Tính"):
    try:
        num1 = int(num1)
        num2 = int(num2)

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "x":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Không thể chia"

        st.write(f"Kết quả: {result}")

    except ValueError:
        st.error("Vui lòng nhập số.")
