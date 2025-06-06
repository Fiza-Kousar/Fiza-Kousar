import streamlit as st
import time
import random

# Hardcoded names
developer_name = "Fiza"  # Change this to your dev's name
your_name = "Fiza Kousar"        # Change this to your name

# Fun royal compliments
praises = [
    "🚀 Oh mighty fixer of bugs, your keyboard is no less than a wand!",
    "🌟 The kingdom of code bows before your debugging might!",
    "👨‍💼 You don’t squash bugs, you *obliterate* them like a true legend!",
    "🎖️ The wise wizard of web apps, healer of HTML hiccups!",
    "🌟 Each bug fears your name, and each feature sings it!"
]

# Funny royal-style response generator
def generate_funny_response(question):
    funny_templates = [
        "Ah, noble query indeed! But why worry when your brilliance shines brighter than the logs on debug mode?",
        "An excellent question, worthy of the highest courts of StackOverflowistan! Let me respond with wit and wisdom...",
        "Oh my dearest code crusader, the answer lies not in the files but in your legendary skills!",
        "Hmm... sounds like a mystery even Sherlock couldn’t trace, but surely you can!",
        "Let’s just say — if answers had royalty, yours would wear the crown!"
    ]
    return random.choice(funny_templates) + f"\n\n> *Your question:* {question}"
          

# Initialize session state
if "access_granted" not in st.session_state:
    st.session_state.access_granted = False

# Streamlit UI
st.set_page_config(page_title="A Special Tribute to Our Star Dev 🚀", page_icon="🚀")
st.title("Welcome to the Bug Fixer’s Den — Where Code Trembles and Bugs Run for Cover! 😎🔥")


if not st.session_state.access_granted:
    # Step 1: Get Dev & Sender Names
    with st.form("entry_form"):
        dev_input = st.text_input("Enter the First name of the one who’s making your day")
        sender_input = st.text_input("Who's the QA that breaks your builds? (Full Name) 💥")
        submitted = st.form_submit_button("Continue")

    if submitted:
        if dev_input.strip() == developer_name and sender_input.strip() == your_name:
            st.session_state.access_granted = True
            st.rerun()  # ✅ Updated for latest Streamlit version
        else:
            st.error("Oops! Looks like your credentials didn't match the royal scrolls. Try again!")


else:
    # Main content
    st.success("Access Granted! Welcome to the Royal Dev Lounge! 🎉")
    time.sleep(1)

    st.markdown("---")
    st.header("👏 A Personal Note to Our Rockstar Dev")


    def type_line(line, delay=0.05):
        placeholder = st.empty()
        text = ""

        # Small initial delay to stabilize rendering before starting
        time.sleep(0.1)

        for i, char in enumerate(line):
            text += char

            # Skip updating on the very first character to reduce flicker
            if i == 0:
                continue

            # Update every 3 characters or at the end
            if i % 3 == 0 or i == len(line) - 1:
                placeholder.markdown(f"**{text}**")
                time.sleep(delay)

        # Make sure full line is shown at the end (in case last update skipped)
        placeholder.markdown(f"**{text}**")



    # Your "typed" message sequence
    typed_lines = [
        f"Hey {developer_name} 🙌",
        "How's life treating you, bug warrior? 🤖",
        "We know these days have been jam-packed with Jira tickets and last-minute commits...",
        "But just so you know — you're not just a dev...",
        "You're *THE DEV*! The beacon of brilliance in this digital storm! 💫"
    ]

    for line in typed_lines:
        type_line(line)
        time.sleep(1)  # Pause between lines

    # Show all compliments
    st.markdown("### 🌟 Your Royal Compliments:")
    for praise in praises:
        st.success(praise)
        time.sleep(1)

    st.markdown("---")
    st.markdown("---")
    st.header("📜 Scroll of Legendary Achievements")

    achievements = [
    "🏅 Knight of No Merge Conflicts",
    "🛡️ Guardian of Clean Code",
    "🪄 Sorcerer of Stack Overflow Scrolls",
    "🐞 Bug Slayer Extraordinaire",
    "📦 Commander of Commits",
    "🔥 Deployer of Dreams (and builds)",
    "🚀 Captain of the Continuous Integration Ship"
] 

    for title in achievements:
        st.balloons()
        st.success(title)
        time.sleep(2)

    st.markdown("---")
    st.caption("Made with ❤️ to celebrate your awesomeness! - Yours truly, Rahul (and ChatGPT)")

    roasts = [
    "😈 Remember, this praise is just a clever disguise so you’ll keep fixing bugs *really fast*. No slacking! 🐢💨",
    "🔥 Excessive awesomeness detected. Side effects include faster bug fixes and occasional eye rolls from your favorite boss. 😏",
    "😜 **FYI:** This royal treatment comes with one secret clause — you owe me *at least* one bug-free sprint. Deal? 🤝",
    "🤡 **Disclaimer:** All compliments here are sponsored by my desperate need for your coding magic. Keep the magic flowing! ✨",
    "🕵️‍♂️ **Note:** If you think this was pure generosity, think again. I’m just investing in my own bug-free future. Smart, right? 😎"
]

    st.markdown("---")
    st.header("⚔️ Hello Dev, Don't be over excited with the Treatement OK")
    for roast in roasts:
        st.markdown(roast)
        time.sleep(1.2)

