import streamlit as st


def add_numbers(a: int, b: int) -> int:

    return a + b


st.title("My First CI/CD Streamlit App")

st.write(
    "Ye app GitHub Actions se test ho rahi hai, aur Streamlit Cloud se auto-deploy!"
)

x = st.number_input("First number", value=1)

y = st.number_input("Second number", value=2)


if st.button("Add"):
    result = add_numbers(x, y)

    st.success(f"Result: {result}")
