import streamlit as st
import requests

st.set_page_config(
    page_title="Multimodal Manufacturing Creator",
    page_icon="⚙️",
    layout="centered",
)

# ── UI ─────────────────────────────────────────
st.title("⚙️ Manufacturing Creator")
st.caption("Multimodal GenAI · Groq + Stability AI")

# ── Sidebar ────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔑 API Keys")

    groq_key = st.text_input("Groq API Key", type="password")
    stability_key = st.text_input("Stability API Key", type="password")

# ── Input ──────────────────────────────────────
prompt = st.text_area(
    "Describe your manufacturing concept",
    placeholder="e.g. AI robotic arm welding car parts in factory...",
    height=120
)

generate_clicked = st.button("⚡ Generate", use_container_width=True)

# ── Groq: Description ──────────────────────────
def generate_description(user_prompt, api_key):
    url = "https://api.groq.com/openai/v1/chat/completions"

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a manufacturing expert. "
                        "Write a professional product description (120-180 words) "
                        "covering features, benefits, and industry use."
                    )
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "temperature": 0.7
        },
        timeout=30
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# ── Stability AI: Image (FINAL FIX 🔥) ──────────
def generate_image(user_prompt, api_key):
    url = "https://api.stability.ai/v2beta/stable-image/generate/core"

    headers = {
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    }

    files = {
        "prompt": (None, f"{user_prompt}, industrial manufacturing, photorealistic, ultra detailed, 4k"),
        "output_format": (None, "png")
    }

    response = requests.post(url, headers=headers, files=files)

    response.raise_for_status()
    return response.content

# ── Generate ───────────────────────────────────
if generate_clicked:
    if not prompt.strip():
        st.warning("Please enter a manufacturing concept.")
    elif not groq_key:
        st.error("Enter Groq API key")
    elif not stability_key:
        st.error("Enter Stability API key")
    else:
        col1, col2 = st.columns(2)

        # Description
        with col1:
            with st.spinner("Generating description..."):
                try:
                    desc = generate_description(prompt, groq_key)
                    st.subheader("📄 Product Description")
                    st.write(desc)
                except Exception as e:
                    st.error(f"Groq Error: {e}")

        # Image
        with col2:
            with st.spinner("Generating image... (~10s)"):
                try:
                    img = generate_image(prompt, stability_key)
                    st.subheader("🖼 Product Image")
                    st.image(img, use_container_width=True)
                except requests.HTTPError as e:
                    code = e.response.status_code
                    if code == 401:
                        st.error("Invalid Stability API key")
                    else:
                        st.error(f"Image Error {code}")
                except Exception as e:
                    st.error(f"Image Error: {e}")