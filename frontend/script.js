const chatMessages = document.getElementById("chatMessages");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");

const API_URL = "http://127.0.0.1:8000/chat";

// Add message bubble
function addMessage(text, sender = "bot") {
  const msg = document.createElement("div");
  msg.className = sender === "user" ? "message user" : "message bot";
  msg.innerText = text;
  chatMessages.appendChild(msg);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Typing indicator
function showTyping() {
  const typing = document.createElement("div");
  typing.className = "message bot typing";
  typing.id = "typing";
  typing.innerText = "AutoStream Assistant is typing...";
  chatMessages.appendChild(typing);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeTyping() {
  const typing = document.getElementById("typing");
  if (typing) typing.remove();
}

// Send message to backend
async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  addMessage(message, "user");
  userInput.value = "";

  showTyping();

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    removeTyping();
    addMessage(data.response, "bot");

  } catch (error) {
    removeTyping();
    addMessage("⚠️ Unable to connect to server. Please try again.", "bot");
    console.error(error);
  }
}

// Button click
sendBtn.addEventListener("click", sendMessage);

// Enter key support
userInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});

// Initial greeting
window.onload = () => {
  addMessage("Hi 👋 I can help you with AutoStream pricing, features, or getting started.");
};
