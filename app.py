import streamlit as st

st.title("Máy tính của Kiều Nga")

# Use float input to handle large numbers and decimals
num1 = st.text_input("Nhập số thứ nhất")
operation = st.selectbox("Chọn phép tính", ("Cộng", "Trừ", "Nhân", "Chia"))
num2 = st.text_input("Nhập số thứ hai")

if st.button("Tính"):
    try:
        # Convert input to float and handle large numbers
        num1 = float(num1.replace(".", ""))
        num2 = float(num2.replace(".", ""))

        result = 0
        if operation == "Cộng":
            result = num1 + num2
        elif operation == "Trừ":
            result = num1 - num2
        elif operation == "Nhân":
            result = num1 * num2
        elif operation == "Chia":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Không thể chia"

        # Format the result with thousand separators
        if isinstance(result, (int, float)):
            # Replace commas with dots in the formatted result
            formatted_result = "{:,.0f}".format(result).replace(",", ".")
            st.write(f"Kết quả: {formatted_result}")
        else:
            st.write(f"Kết quả: {result}")

    except ValueError:
        st.error("Vui lòng nhập số.")
