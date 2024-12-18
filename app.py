import streamlit as st

def main():
    # Set the title of the app
    st.title("Simple Calculator App")

    # Input fields for numbers
    st.write("Enter two numbers to perform basic arithmetic operations:")
    
    num1 = st.number_input("Enter the first number:", value=0.0, step=0.1)
    num2 = st.number_input("Enter the second number:", value=0.0, step=0.1)

    # Dropdown menu for selecting the operation
    operation = st.selectbox("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform calculation when the button is clicked
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
            st.success(f"The result of addition is: {result}")

        elif operation == "Subtract":
            result = num1 - num2
            st.success(f"The result of subtraction is: {result}")

        elif operation == "Multiply":
            result = num1 * num2
            st.success(f"The result of multiplication is: {result}")

        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
                st.success(f"The result of division is: {result}")
            else:
                st.error("Division by zero is not allowed.")

if __name__ == "__main__":
    main()
