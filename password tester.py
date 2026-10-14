# Password Strenght Checker

import streamlit as st
import string

st.title("Password Strength Checker")
st.write("Enter a password to test its strength.")

# Get password from the user
user_input = st.text_input("Enter a password:", type="password")

if user_input:
    # Check password conditions
    total_characters = len(user_input)
    has_uppercase = any(char.isupper() for char in user_input)
    has_lowercase = any(char.islower() for char in user_input)
    has_digit = any(char.isdigit() for char in user_input)
    has_special = any(char in string.punctuation for char in user_input)

    # Display individual checks
    st.subheader("Password Requirements")

    if total_characters >= 8:
        st.success("✓ At least 8 characters")
    else:
        st.error("✗ Password must have at least 8 characters")

    if has_uppercase:
        st.success("✓ Contains an uppercase letter")
    else:
        st.error("✗ Add at least one uppercase letter")

    if has_lowercase:
        st.success("✓ Contains a lowercase letter")
    else:
        st.error("✗ Add at least one lowercase letter")

    if has_digit:
        st.success("✓ Contains a number")
    else:
        st.error("✗ Add at least one digit (0-9)")

    if has_special:
        st.success("✓ Contains a special character")
    else:
        st.error("✗ Add at least one special character (!, @, #, etc.)")

    # Overall password strength
    if (
        total_characters >= 8
        and has_uppercase
        and has_lowercase
        and has_digit
        and has_special
    ):
        st.success("Strong password! All requirements are satisfied.")
    else:
        st.warning("Weak password. Please meet all the requirements.")
