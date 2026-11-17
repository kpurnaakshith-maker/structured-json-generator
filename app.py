
import streamlit as st
import json

from extractor import extract_product_information


# Page configuration
st.set_page_config(
    page_title="AI JSON Generator",
    page_icon="🤖",
    layout="centered"
)


# Application heading
st.title("🤖 Structured JSON Output Generator")

st.write(
    "Convert unstructured product descriptions "
    "into structured JSON using Ollama and Qwen 3.5."
)

st.divider()


# Product description input
st.subheader("Enter Product Information")

product_text = st.text_area(
    "Product Description",
    placeholder=(
        "Example: Samsung Galaxy S25, 256GB storage, "
        "blue colour, price Rs. 85000, 50MP camera."
    ),
    height=150
)


# Generate JSON button
if st.button("Generate JSON", type="primary"):

    if not product_text.strip():

        st.warning("Please enter a product description.")

    else:

        with st.spinner("Qwen 3.5 is extracting information..."):

            try:

                product = extract_product_information(product_text)

                # Convert Pydantic model into dictionary
                result = product.model_dump()

                # Convert dictionary into JSON
                json_result = json.dumps(
                    result,
                    indent=4,
                    ensure_ascii=False
                )

                st.success("JSON generated and validated successfully!")

                st.subheader("Generated JSON")

                st.code(json_result, language="json")

                # Download JSON file
                st.download_button(
                    label="Download JSON",
                    data=json_result,
                    file_name="product_information.json",
                    mime="application/json"
                )

                with st.expander("View extracted fields"):
                    st.json(result)

            except Exception as error:

                st.error("Unable to generate valid JSON.")
                st.exception(error)


# Footer
st.divider()

st.caption(
    "Powered by Python | Ollama | Qwen 3.5 | Pydantic | Streamlit"
)
